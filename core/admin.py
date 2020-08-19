# core/admin.py

from django.contrib import admin
from .models import Recipe, Lineup  # add this
# Register your models here.

admin.site.register(Recipe) # add this
admin.site.register(Lineup) # add this