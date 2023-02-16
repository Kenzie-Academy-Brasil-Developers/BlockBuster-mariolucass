from rest_framework import serializers
from .models import Movie, MovieRating, MovieOrder


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127, required=True)
    duration = serializers.CharField(max_length=10, required=False)
    rating = serializers.ChoiceField(choices=MovieRating.choices, default=MovieRating.DEFAULT)
    synopsis = serializers.CharField(required=False)
    added_by = serializers.SerializerMethodField()

    def create(self, validated_data) -> Movie:
        return Movie.objects.create(**validated_data)

    def get_added_by(self, obj):
        return obj.user.email


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_at = serializers.DateTimeField(read_only=True)
    buyed_by = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()

    def create(self, validated_data) -> Movie:
        return MovieOrder.objects.create(**validated_data)

    def get_buyed_by(self, obj):
        return obj.user.email

    def get_title(self, obj):
        return obj.movie.title
