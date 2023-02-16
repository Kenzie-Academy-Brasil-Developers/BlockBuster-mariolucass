from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Movie, MovieRating


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    duration = serializers.CharField(max_length=20, required=False)
    rating = serializers.ChoiceField(choices=MovieRating.choices, default=MovieRating.DEFAULT)
    synopsis = serializers.CharField(required=False)

    user = UserSerializer(write_only=True, required=False)
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, obj):
        return obj.user.email

    def create(self, validated_data) -> Movie:
        print(validated_data)
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    price = serializers.CharField(read_only=True)
    buyed_at = serializers.DateTimeField()

    user = UserSerializer(write_only=True)
    movie = MovieSerializer(write_only=True)

    buyed_by = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()

    def get_buyed_by(self, obj):
        return obj.user.email

    def get_title(self, obj):
        return obj.book.title

    def create(self, validated_data) -> Movie:
        return Movie.objects.create(**validated_data)
