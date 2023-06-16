from django.conf import settings
from django.db import models
from django.db.models import Q, OuterRef, Subquery, Case, When
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie, Category, Actor, Genre, Rating, Reviews
from .forms import ReviewForm


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
