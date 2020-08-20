# core/views.py

from rest_framework import viewsets
from .serializers import RecipeSerializer, PlatinumLineupSerializer, SilverLineupSerializer
from .models import Recipe, PlatinumLineup, SilverLineup

class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

class PlatinumLineupViewSet(viewsets.ModelViewSet):
    serializer_class = PlatinumLineupSerializer
    queryset = PlatinumLineup.objects.all()

class SilverLineupViewSet(viewsets.ModelViewSet):
    serializer_class = SilverLineupSerializer
    queryset = SilverLineup.objects.all()