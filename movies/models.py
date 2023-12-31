from django.db import models
from datetime import date

from django.urls import reverse


class Category(models.Model):
    # Категорії
    name = models.CharField("Категорія", max_length=150)
    description = models.TextField("Опис")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорії"
        verbose_name_plural = "Категорії"


class Actor(models.Model):
    # Актори та режисери
    name = models.CharField("Ім'я", max_length=100)
    age = models.PositiveSmallIntegerField("Вік", default=0)
    description = models.TextField("Опис")
    image = models.ImageField("Зображення", upload_to="actors/")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('actor_detail', kwargs={"slug": self.name})

    class Meta:
        verbose_name = "Актори та режисери"
        verbose_name_plural = "Актори та режисери"


class Genre(models.Model):
    # Жанри
    name = models.CharField("Ім'я", max_length=100)
    description = models.TextField("Опис")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанри"


class Movie(models.Model):
    # Фільм
    title = models.CharField("Назва", max_length=100)
    tagline = models.CharField("Слоган", max_length=100, default='')
    description = models.TextField("Опис")
    poster = models.ImageField("Постер", upload_to="movies/")
    year = models.PositiveSmallIntegerField("Дата виходу", default=2019)
    country = models.CharField("Країна", max_length=30)
    directors = models.ManyToManyField(
        Actor, verbose_name="режисер", related_name="film_director")
    actors = models.ManyToManyField(
        Actor, verbose_name="актори", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="жанри")
    world_premiere = models.DateField("Прем'єра в світі", default=date.today)
    budget = models.PositiveIntegerField("Бюджет", default=0,
                                         help_text="Вказувати суму в доларах")
    fees_in_usa = models.PositiveIntegerField(
        "Сбори в США", default=0, help_text="Вказувати суму в доларах"
    )
    fess_in_world = models.PositiveIntegerField(
        "Сбори в світі", default=0, help_text="Вказувати суму в доларах"
    )
    category = models.ForeignKey(
        Category, verbose_name="Категорії", on_delete=models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Чернетка", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Фільм"
        verbose_name_plural = "Фільми"


class MovieShots(models.Model):
    # Кадри з Фільму
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Опис")
    image = models.ImageField("Зображення", upload_to="movie_shots/")
    movie = models.ForeignKey(
        Movie, verbose_name="Фільм", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр из фільму"
        verbose_name_plural = "Кадри из фільму"


class RatingStar(models.Model):
    # Зірка рейтингу
    value = models.SmallIntegerField("Значення", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Зірка рейтингу"
        verbose_name_plural = "Зірка рейтингу"
        ordering = ["-value"]


class Rating(models.Model):
    # Рейтинг
    ip = models.CharField("IP адреса", max_length=15)
    star = models.ForeignKey(
        RatingStar, on_delete=models.CASCADE, verbose_name="зірка")
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, verbose_name="фільм", related_name="ratings")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):
    # Відгуки
    email = models.EmailField()
    name = models.CharField("Ім'я", max_length=100)
    text = models.TextField("Повідомлення", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родич", on_delete=models.SET_NULL, blank=True, null=True
    )
    movie = models.ForeignKey(
        Movie, verbose_name="Фільм", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"
