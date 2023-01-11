from django.db import models
from django.contrib.auth.models import User


class Account(User):

    def __str__(self):
        return self.first_name

