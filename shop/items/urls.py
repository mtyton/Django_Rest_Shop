from django.urls import path, include
from rest_framework import routers
from .views import CategoriesView, ItemsView

router = routers.DefaultRouter()
router.register('categories', CategoriesView)
router.register('items', ItemsView)

urlpatterns = [
    path('', include(router.urls)),

]