from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate

from rest_framework.views import APIView, Response, Request
from rest_framework.pagination import PageNumberPagination


from .models import User
from .serializers import UserSerializer
from .utils import update_keys, verify_user_exists
from .exceptions import UserException

from utils.methods import generate_response, generate_delete_response, generate_error_response


class UserView(APIView, PageNumberPagination):
    def get(self, request: Request):
        if request.query_params:
            users = User.objects.filter().order_by("id")
        else:
            users = User.objects.all().order_by("id")

        serializer = UserSerializer(users, many=True)

        return generate_response(200, serializer.data)

    def post(self, request: Request):
        if "email" in request.data and "username" in request.data:
            try:
                verify_user_exists(request.data["email"], request.data["username"])
            except UserException as e:
                return generate_error_response(400, e.message)

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return generate_response(201, serializer.data)


class UserDetailView(APIView):
    def get(self, request: Request, user_id: int):
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(data=user)

        return generate_response(200, serializer.data)

    def patch(self, request: Request, user_id: int):
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(data=user)
        update_keys(serializer.data.items(), user)

        serializer.save()

        return generate_response(200, serializer.data)

    def delete(self, request: Request, user_id: int):
        user = get_object_or_404(User, id=user_id)
        user.delete()

        return generate_delete_response()
