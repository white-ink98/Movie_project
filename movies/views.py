from django.shortcuts import render, redirect
from django.views.generic.base import View

from .models import Movie


class MoviesView(GenreYear, ListView):
    # Список фільмів
    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    # Повний опис
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    slug_field = "url"


class AddReview(View):
    # Відгуки
    def post(self, request, pk):
        print(request.POST)
        return redirect("/")
