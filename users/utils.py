from rest_framework.views import Response, status
from .models import User
from .exceptions import UserException
from utils.methods import generate_error_response


class MessageErrors:
    error_email_and_username = {"email": ["email already registered."], "username": ["username already taken."]}
    error_email = {"email": ["email already registered."]}
    error_username = {"username": ["username already taken."]}


def update_keys(keys, user):
    for key, value in keys:
        if key != id:
            setattr(user, key, value)


def find_user(id):
    try:
        return User.objects.get(id=id)
    except User.DoesNotExist:
        return None


def verify_user_exists(
    email,
    username,
):
    arr = []
    try:
        User.objects.get(email=email)
        arr.append("email registered")
    except User.DoesNotExist:
        pass

    try:
        User.objects.get(username=username)
        arr.append("username registered")
    except User.DoesNotExist:
        pass

    match (len(arr)):
        case 0:
            pass
        case 1:
            if arr[0] == "email registered":
                raise UserException(MessageErrors.error_email)
            raise UserException(MessageErrors.error_username)
        case 2:
            raise UserException(MessageErrors.error_email_and_username)
