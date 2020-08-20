
# core/models.py

from django.db import models
# Create your models here.

class Recipe(models.Model):
    DIFFICULTY_LEVELS = (
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    )
    name = models.CharField(max_length=120)
    ingredients = models.CharField(max_length=400)
    picture = models.FileField()
    difficulty = models.CharField(choices=DIFFICULTY_LEVELS, max_length=10)
    prep_time = models.PositiveIntegerField()
    prep_guide = models.TextField()
    
    def __str__(self):
        return "Recipe for {}".format(self.name)

class PlatinumLineup(models.Model):

    player = models.CharField(default='player', max_length=1000)
    team = models.CharField(default='team', max_length=1000)
    position = models.CharField(default='position', max_length=1000)
    projection = models.CharField(default='projection', max_length=1000)
    salary = models.CharField(default='salary', max_length=1000)
    std = models.CharField(default='std' , max_length=1000)
    
    def __str__(self):
        return "Lineup for {}".format(self.player)

class SilverLineup(models.Model):

    player = models.CharField(default='player', max_length=1000)
    team = models.CharField(default='team', max_length=1000)
    position = models.CharField(default='position', max_length=1000)
    projection = models.CharField(default='projection', max_length=1000)
    salary = models.CharField(default='salary', max_length=1000)
    std = models.CharField(default='std' , max_length=1000)
    
    def __str__(self):
        return "Lineup for {}".format(self.player)

