# core/serializers.py

from rest_framework import serializers
from .models import Recipe, Lineup
class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ("id", "name", "ingredients", "picture", "difficulty", "prep_time", "prep_guide")

class LineupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lineup
        fields = ('id', 'player', 'team', 'position', 'projection', 'salary', 'std', 'pk')