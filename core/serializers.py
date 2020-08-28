# core/serializers.py

from rest_framework import serializers
from .models import Recipe, PlatinumLineup, GoldLineup, SilverLineup, BronzeLineup, SlateSunMon
class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ("id", "name", "ingredients", "picture", "difficulty", "prep_time", "prep_guide")

class PlatinumLineupSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlatinumLineup
        fields = ('id', 'player', 'team', 'position', 'projection', 'salary', 'stdev', 'pk')

class GoldLineupSerializer(serializers.ModelSerializer):

    class Meta:
        model = GoldLineup
        fields = ('id', 'player', 'team', 'position', 'projection', 'salary', 'stdev', 'pk')

class SilverLineupSerializer(serializers.ModelSerializer):

    class Meta:
        model = SilverLineup
        fields = ('id', 'player', 'team', 'position', 'projection', 'salary', 'stdev', 'pk')

class BronzeLineupSerializer(serializers.ModelSerializer):

    class Meta:
        model = BronzeLineup
        fields = ('id', 'player', 'team', 'position', 'projection', 'salary', 'stdev', 'pk')

class SlateSunMonSerializer(serializers.ModelSerializer):

    class Meta:
        model = SlateSunMon
        fields = ('id', 'player', 'team', 'position', 'projection', 'salary', 'stdev', 'pk')