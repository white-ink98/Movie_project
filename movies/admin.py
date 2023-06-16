from django.contrib import admin
from .models import Category, Genre, Movie, MovieShots, Actor, RatingStar, Reviews


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ("name", "url")
    list_display_links = ("name",)


@admin.register(Movie)
class MovieAdmin(TranslationAdmin):
    list_display = ("title", "category", "url", "draft")
    list_filter = ("category", "year")
    search_fields = ("title", "category__name")


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "movie", "id")
    readonly_fields = ("name", "email")
    # приховані від редагування


# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Genre)
# admin.site.register(Movie)
# admin.site.register(MovieShots)
# admin.site.register(Actor)
# admin.site.register(RatingStar)
# admin.site.register(Reviews)
