from .models import Movie
from .exceptions import MovieException
from utils.methods import MessageErrors


def update_keys(keys, movie):
    for key, value in keys:
        if key != id:
            setattr(movie, key, value)
