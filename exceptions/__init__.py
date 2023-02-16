class MovieException(Exception):
    def __init__(self, message):
        self.message = message


class UserException(Exception):
    def __init__(self, message):
        self.message = message
