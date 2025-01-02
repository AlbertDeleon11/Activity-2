from django.contrib import admin
from .models import UserProfile, Recipe, Pastry, Rating, BakingTip, Comment, Category

admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Pastry)
admin.site.register(Rating)
admin.site.register(BakingTip)
admin.site.register(Comment)
