from django.contrib import admin
from .models import Category, Genre, Movie, MovieShots, Actor, RatingStar, Reviews


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "id")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Actor)
admin.site.register(RatingStar)
admin.site.register(Reviews)
