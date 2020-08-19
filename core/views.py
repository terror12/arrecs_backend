# core/views.py

from rest_framework import viewsets
from .serializers import RecipeSerializer, LineupSerializer
from .models import Recipe, Lineup

class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

class LineupViewSet(viewsets.ModelViewSet):
    serializer_class = LineupSerializer
    queryset = Lineup.objects.all()