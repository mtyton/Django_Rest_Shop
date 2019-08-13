from django.urls import path, include
from rest_framework import routers
from .views import CategoriesView, ItemsView

router = routers.DefaultRouter()
router.register('categories', CategoriesView, basename="categories")
router.register('items', ItemsView, basename="items")

urlpatterns = [
    path('', include(router.urls)),

]