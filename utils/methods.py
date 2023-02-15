from rest_framework.views import Response, status


def handle_exception(exception):
    ...


def generate_response(status_code, variant):
    match status_code:
        case 200:
            status_code = status.HTTP_200_OK
        case 201:
            status_code = status.HTTP_201_CREATED
    return Response(variant, status_code)


def generate_delete_response():
    return Response(status=status.HTTP_204_NO_CONTENT)


def generate_error_response(status_code, err_message: str or dict):
    match status_code:
        case 400:
            status_code = status.HTTP_400_BAD_REQUEST
        case 401:
            status_code = status.HTTP_401_UNAUTHORIZED
        case 402:
            status_code = status.HTTP_402_PAYMENT_REQUIRED
        case 403:
            status_code = status.HTTP_403_FORBIDDEN
        case 404:
            status_code = status.HTTP_404_NOT_FOUND
        case 409:
            status_code = status.HTTP_409_CONFLICT

    if err_message is str:
        dict_message_error = {"error": err_message}
    else:
        dict_message_error = err_message

    return Response(dict_message_error, status=status_code)
