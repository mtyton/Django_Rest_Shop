from django.urls import path, include
from rest_framework import routers
from .views import CategoriesView, ItemsView

router = routers.DefaultRouter()
router.register('categories', CategoriesView, base_name="category")
router.register('items', ItemsView, base_name="items")

urlpatterns = [
    path('', include(router.urls)),

]