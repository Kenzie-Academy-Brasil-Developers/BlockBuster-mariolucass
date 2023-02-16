from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(max_length=127)
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(required=False)
    is_superuser = serializers.BooleanField(read_only=True)
    is_employee = serializers.BooleanField(default=False)

    def create(self, validated_data) -> User:
        return (
            User.objects.create_superuser(**validated_data)
            if validated_data["is_employee"] == True
            else User.objects.create_user(**validated_data)
        )

    def update(self, validated_data) -> User:
        keys = validated_data.items()

        # for key, value in keys:
        #     if key != id:
        #         setattr(user, key, value)

        ...
