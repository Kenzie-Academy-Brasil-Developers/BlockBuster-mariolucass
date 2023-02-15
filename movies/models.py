from django.db import models
from users.models import User


class MovieRating(models.TextChoices):
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"
    DEFAULT = "G"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10)
    rating = models.CharField(max_length=20, choices=MovieRating.choices, default=MovieRating.DEFAULT)
    synopsis = models.TextField(null=True)
    users = models.ManyToManyField("users.User", through="movies.MovieOrder", related_name="movies")

    def __repr__(self):
        id_movie = self.id
        name_movie = self.name
        return f"<{[id_movie]}, movie: {name_movie};>"

    def __str__(self):
        return f" Movie[{self.id}] -> {self.name}"


class MovieOrder(models.Model):
    price = models.IntegerField()

    buyed_at = models.DateField(max_length=20)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="movie_orders")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="orders")

    def __repr__(self):
        id_order = self.id
        user_buyer = self.user.objects.all()[0].name
        movie_sold = self.movie.objects.all()[0].name
        buyed_at = self.buyed_at
        return f"<Order{[id_order]}, The user {user_buyer} buys {movie_sold} at {buyed_at}.>"

    def __str__(self):
        id_order = self.id
        user_buyer = self.user.objects.all()[0].name
        movie_sold = self.movie.objects.all()[0].name
        return f" MovieOrder[{id_order}] -> {movie_sold}, {user_buyer}"
