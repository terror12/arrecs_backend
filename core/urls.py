# core/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, LineupViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)
router.register(r'lineups', LineupViewSet)

urlpatterns = [
    path("", include(router.urls))
]