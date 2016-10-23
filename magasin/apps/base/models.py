from django.db import models
from django.contrib.auth.models import AbstractUser


class APIUser(AbstractUser):
    """
    API user representation.
    """
    email = models.EmailField(max_length=255, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_username(self):
        return self.email

