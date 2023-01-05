from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'phone', 'email',]

    def __str__(self):
        return self.first_name
