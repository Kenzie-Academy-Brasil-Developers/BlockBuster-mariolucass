from django.shortcuts import get_object_or_404

from rest_framework.views import APIView, Request
from rest_framework_simplejwt.authentication import JWTAuthentication


from .models import User
from .serializers import UserSerializer
from .utils import update_keys, verify_user_exists
from .exceptions import UserException

from utils.methods import generate_response, generate_delete_response, generate_error_response
from utils.permissions import EmployeeOrOwnerPermissions


class UserView(APIView):
    def get(self, request: Request):
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
    authentication_classes = [JWTAuthentication]
    permission_classes = [EmployeeOrOwnerPermissions]

    def get(self, request: Request, user_id: int):
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(user)
        return generate_response(200, serializer.data)

    def patch(self, request: Request, user_id: int):
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)

        user_body = serializer.validated_data

        update_keys(user_body.items(), user)

        serializer.save()

        return generate_response(200, serializer.data)

    def delete(self, request: Request, user_id: int):
        user = get_object_or_404(User, id=user_id)
        user.delete()

        return generate_delete_response()
