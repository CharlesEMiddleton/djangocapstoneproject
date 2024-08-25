from django.contrib import admin

# Register your models here.
from .models import RecipeRequirement, MenuItem, Ingredient, Purchase

[admin.site.register(X) for X in [RecipeRequirement, MenuItem, Ingredient, Purchase]]