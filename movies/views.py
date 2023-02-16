from django.shortcuts import get_object_or_404

from rest_framework.views import APIView, Request
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication


from .permissions import EmployeeOrReadOnlyPermissions
from .models import Movie
from .serializers import MovieSerializer
from .utils import update_keys

from utils.methods import generate_response, generate_delete_response


class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [EmployeeOrReadOnlyPermissions]

    def get(self, request: Request):
        if request.query_params:
            movies = Movie.objects.filter().order_by("id")
        else:
            movies = Movie.objects.all().order_by("id")

        result_page = self.paginate_queryset(movies, request, view=self)
        serializer = MovieSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, request: Request):
        print(request.user)
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

    def patch(self, request: Request, movie_id: int):
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(movie)

        update_keys(serializer.items(), movie)

        movie.save()
        return generate_response(200, serializer.data)

    def delete(self, request: Request, movie_id: int):
        movie = get_object_or_404(Movie, id=movie_id)

        movie.delete()
        return generate_delete_response()


class MovieOrderView(APIView):
    def post(self, request: Request):
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset, many=True)

        return generate_response(201, serializer.data)
