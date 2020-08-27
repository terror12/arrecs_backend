# core/admin.py

from django.contrib import admin
from .models import Recipe, PlatinumLineup, GoldLineup, SilverLineup, BronzeLineup, SlateSunMon  # add this
# Register your models here.

admin.site.register(Recipe) # add this
admin.site.register(PlatinumLineup) # add this
admin.site.register(GoldLineup) # add this
admin.site.register(SilverLineup) # add this
admin.site.register(BronzeLineup) # add this
admin.site.register(SlateSunMon) # add this