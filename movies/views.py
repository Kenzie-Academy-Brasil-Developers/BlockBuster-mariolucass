from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from utils.methods import generate_response, generate_delete_response
from utils.permissions import EmployeeOrReadOnlyPermissions, AuthenticatedPermissions
from .models import Movie
from .serializers import MovieSerializer, MovieOrderSerializer


class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [EmployeeOrReadOnlyPermissions]

    def get(self, request: Request):
        movies = Movie.objects.filter().order_by("id") if request.query_params else Movie.objects.all().order_by("id")

        result_page = self.paginate_queryset(movies, request, view=self)
        serializer = MovieSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, request: Request):
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user)

        return generate_response(201, serializer.data)


class MovieDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [EmployeeOrReadOnlyPermissions]

    def get(self, request: Request, movie_id: int):
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(movie)

        return generate_response(200, serializer.data)

    def delete(self, request: Request, movie_id: int):
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()

        return generate_delete_response()


class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AuthenticatedPermissions]

    def post(self, request: Request, movie_id: int):
        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        movie = get_object_or_404(Movie, id=movie_id)

        serializer.save(user=request.user, movie=movie)

        return generate_response(201, serializer.data)
