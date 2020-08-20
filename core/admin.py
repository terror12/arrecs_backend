# core/admin.py

from django.contrib import admin
from .models import Recipe, PlatinumLineup, SilverLineup  # add this
# Register your models here.

admin.site.register(Recipe) # add this
admin.site.register(PlatinumLineup) # add this
admin.site.register(SilverLineup) # add this