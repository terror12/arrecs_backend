# core/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, PlatinumLineupViewSet, GoldLineupViewSet, SilverLineupViewSet, BronzeLineupViewSet, SlateSunMonViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)
router.register(r'platinumlineup', PlatinumLineupViewSet)
router.register(r'goldlineup', GoldLineupViewSet)
router.register(r'silverlineup', SilverLineupViewSet)
router.register(r'bronzelineup', BronzeLineupViewSet)
router.register(r'slatesunmon', SlateSunMonViewSet)

urlpatterns = [
    path("", include(router.urls))
]