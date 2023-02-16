from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Movie, MovieRating, MovieOrder


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127, required=True)
    duration = serializers.CharField(max_length=10, required=False)
    rating = serializers.ChoiceField(choices=MovieRating.choices, default=MovieRating.DEFAULT)
    synopsis = serializers.CharField(required=False)

    user = UserSerializer(write_only=True, required=False)
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, obj):
        return obj.user.email

    def create(self, validated_data) -> Movie:
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_at = serializers.DateField(read_only=True)

    user = UserSerializer(write_only=True, required=False)
    movie = MovieSerializer(write_only=True, required=False)

    buyed_by = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()

    def get_buyed_by(self, obj):
        return obj.user.email

    def get_title(self, obj):
        return obj.movie.title

    def create(self, validated_data) -> Movie:
        return MovieOrder.objects.create(**validated_data)
