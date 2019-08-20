import json
from django.test import TestCase
from rest_framework.test import APIClient, APIRequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from .views import CategoriesView
from .models import Category, Item
from .serializers import CategorySerialzier


class TestCategories(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.serialzier = CategorySerialzier()
        self.test_user = User.objects.create_superuser(username="admin", password="admin", email="admin@email.com")
        c = Category(name="test_category", pid=None)
        c.save()

    def test_get(self):
        url = reverse("category-list")
        response = self.client.get(url, format=json)
        self.assertEqual(response.status_code, 200)
        response.render()
        self.assertNotEqual(response.content, None)

    def test_no_auth_post(self):
        url = reverse("category-list")
        c = Category(name="test_post_category", pid=None)
        response = self.client.post(url, json={'name':"test__post", 'pid':None})
        self.assertEqual(response.status_code, 403)

    def test_post_auth(self):
        url = reverse("category-list")
        c = Category(name="test_post_category", pid=None)
        self.client.login(username="admin", password="admin")
        self.client.force_authenticate(user=self.test_user)
        response = self.client.post(url, {'name':"test__post", 'pid':None}, format='json')
        self.assertEqual(response.status_code, 201)


class TestItemView(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.test_user = User.objects.create_superuser(username="admin", password="admin", email="admin@email.com")
        c = Category(name="test_category", pid=None)
        c.save()
        i = Item(name="test_item", price=20, available=True)
        i.save()

    def test_get(self):
        url = reverse("items-list")
        response = self.client.get(url, format=json)
        self.assertEqual(response.status_code, 200)
        response.render()
        self.assertNotEqual(response.content, None)

    def test_no_auth_post(self):
        url = reverse("items-list")
        response = self.client.post(url, {'categories':None, 'name':"testItem", 'price':23, 'available':True},
                                    format="json")
        self.assertEqual(response.status_code, 403)

    def test_post_auth(self):
        # TODO fix the request
        url = reverse("items-list")
        self.client.login(username="admin", password="admin")
        response = self.client.post(url, {'categories':None,'name': "testItem", 'price': 23, 'available': True},
                                    format="json")
        #print(response)


class TestItemModel(TestCase):
    def setUp(self):
        self.model = Item()

    def test_adding(self):
        item = Item(name="adding_test", price=23, available=True)
        item.save()
        check = Item.objects.filter(name="adding_test")
        self.assertEqual(item, check[0])


class TestCategoryModel(TestCase):
    def test_pid_nullability(self):
        category = Category(name="what?", pid=None)
        category.save()
        check = Category.objects.filter(name="what?")
        self.assertEqual(category, check[0])
        self.assertEqual(category.pid, None)


class TestCategorySerializer(TestCase):
    def setUp(self):
        self.serializer = CategorySerialzier()

    def test_get_subcategories(self):
        new_category = Category(name="new_category", pid=None)
        new_category.save()
        new_subcategory = Category(name="subcategory", pid=new_category)
        new_subcategory.save()
        subs = self.serializer.get_subcategories(new_category)
        self.assertEqual(len(subs), 1)
        self.assertEqual(subs[0], new_subcategory.name)

    def test_get_belonging_items(self):
        new_category = Category(name="new_category", pid=None)
        new_category.save()
        items = self.serializer.get_belonging_items(new_category)
        self.assertEqual(len(items), 0)
        item = Item(id=0, name="test_item", price=43, available=True)
        item.save()
        item.categories.add(new_category)
        items = self.serializer.get_belonging_items(new_category)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0], item.name)