# core/views.py

from rest_framework import viewsets
from .serializers import RecipeSerializer, PlatinumLineupSerializer, GoldLineupSerializer, SilverLineupSerializer, BronzeLineupSerializer, SlateSunMonSerializer
from .models import Recipe, PlatinumLineup, GoldLineup, SilverLineup, BronzeLineup, SlateSunMon

class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

class PlatinumLineupViewSet(viewsets.ModelViewSet):
    serializer_class = PlatinumLineupSerializer
    queryset = PlatinumLineup.objects.all()

class GoldLineupViewSet(viewsets.ModelViewSet):
    serializer_class = GoldLineupSerializer
    queryset = GoldLineup.objects.all()

class SilverLineupViewSet(viewsets.ModelViewSet):
    serializer_class = SilverLineupSerializer
    queryset = SilverLineup.objects.all()

class BronzeLineupViewSet(viewsets.ModelViewSet):
    serializer_class = BronzeLineupSerializer
    queryset = BronzeLineup.objects.all()

class SlateSunMonViewSet(viewsets.ModelViewSet):
    serializer_class = SlateSunMonSerializer
    queryset = SlateSunMon.objects.all()