from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=64, unique=True)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return f'{self.username}'


