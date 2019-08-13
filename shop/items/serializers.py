from rest_framework import serializers
from .models import Category, Item


class CategorySerialzier(serializers.HyperlinkedModelSerializer):
    subcategories = serializers.SerializerMethodField()
    belonging_items = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_subcategories(self, obj):
        queryset= Category.objects.all().filter(pid=obj)
        subs = []
        for q in queryset:
            subs.append(q.name)
        return subs

    def get_belonging_items(self, obj):
        queryset = Item.objects.all().filter(categories__name__contains=obj.name)
        subs = []
        for q in queryset:
            subs.append(q.name)
        return subs


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['categories','name', 'price', 'available']
