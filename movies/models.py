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
    duration = models.CharField(max_length=10, null=True, blank=True)
    rating = models.CharField(max_length=20, choices=MovieRating.choices, default=MovieRating.DEFAULT)
    synopsis = models.TextField(null=True, blank=True)

    user = models.ForeignKey(User, related_name="movies", on_delete=models.CASCADE)
    orders = models.ManyToManyField("users.User", related_name="orders", through="movies.MovieOrder")

    def __repr__(self):
        id_movie = self.id
        name_movie = self.title
        return f"<{[id_movie]}, movie: {name_movie};>"

    def __str__(self):
        id_movie = self.id
        name_movie = self.title
        return f" Movie[{id_movie}] -> {name_movie}"


class MovieOrder(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=2)
    buyed_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __repr__(self):
        id_order = self.id
        user_buyer = self.user.username
        movie_sold = self.movie.title
        buyed_at = self.buyed_at

        return f"<Order{[id_order]}, The user {user_buyer} bought {movie_sold} at {buyed_at}.>"

    def __str__(self):
        id_order = self.id
        user_buyer = self.user.username
        movie_sold = self.movie.title

        return f" MovieOrder[{id_order}] -> {movie_sold}, {user_buyer}"
