from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=127, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField(blank=True, null=True)
    is_employee = models.BooleanField(default=False)

    def __repr__(self):
        id_user = self.id
        name_user = self.name
        email_user = self.email

        return f"<{[id_user]}, name: {name_user}; email:{email_user}>"

    def __str__(self):
        return f" User[{self.id}] -> {self.name}; {self.email}"
