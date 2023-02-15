from rest_framework.views import Response, status
from .models import Movie


def update_keys(keys, movie):
    for key, value in keys:
        if key != id:
            setattr(movie, key, value)


def find_movie(id):
    try:
        return Movie.objects.get(id=id)

    except Movie.DoesNotExist:
        return None
