from utils.methods import MessageErrors
from users.models import User
from exceptions import UserException


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
