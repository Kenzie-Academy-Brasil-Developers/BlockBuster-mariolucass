from django.shortcuts import get_object_or_404

from rest_framework.views import APIView, Response, Request
from rest_framework.pagination import PageNumberPagination

from .models import Movie

# from .utils import
from .serializers import MovieSerializer


class MovieView(APIView):
    def get(self, request: Request):
        if request.query_params:
            ...
        else:
            ...

        return Response(status=200)

    def post(self, request: Request):
        serializer = MovieSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        ...
        return Response(serializer.data, status=201)


class MovieDetailView(APIView):
    def get(self, request: Request, user_id: int):
        movie = get_object_or_404(Movie, id=user_id)
        serializer = MovieSerializer(movie)

        ...
        return Response(serializer.data, status=200)

    def patch(self, request: Request, user_id: int):
        movie = get_object_or_404(Movie, id=user_id)
        serializer = MovieSerializer(movie)

        for key, value in serializer.items():
            setattr(movie, key, value)

        ...
        return Response(serializer.data, status=200)

    def delete(self, request: Request, user_id: int):
        movie = get_object_or_404(Movie, id=user_id)
        serializer = MovieSerializer(movie)

        movie.delete()
        return Response(status=204)
