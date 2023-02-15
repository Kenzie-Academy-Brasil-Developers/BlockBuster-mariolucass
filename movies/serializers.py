from rest_framework import serializers
from .models import Movie, MovieRating
from users.serializers import UserSerializer


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.IntegerField(read_only=True)
    duration = serializers.CharField(max_length=20)
    rating = serializers.EmailField()
    synopsis = serializers.ChoiceField(choices=MovieRating.choices, default=MovieRating.DEFAULT)
    users = UserSerializer(many=True)

    def create(self, validated_data) -> Movie:
        return Movie.objects.create(**validated_data)
