# core/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, PlatinumLineupViewSet, SilverLineupViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)
router.register(r'platinumlineup', PlatinumLineupViewSet)
router.register(r'silverlineup', SilverLineupViewSet)

urlpatterns = [
    path("", include(router.urls))
]