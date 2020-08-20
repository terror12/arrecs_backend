# core/serializers.py

from rest_framework import serializers
from .models import Recipe, PlatinumLineup, SilverLineup
class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ("id", "name", "ingredients", "picture", "difficulty", "prep_time", "prep_guide")

class PlatinumLineupSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlatinumLineup
        fields = ('id', 'player', 'team', 'position', 'projection', 'salary', 'std', 'pk')

class SilverLineupSerializer(serializers.ModelSerializer):

    class Meta:
        model = SilverLineup
        fields = ('id', 'player', 'team', 'position', 'projection', 'salary', 'std', 'pk')