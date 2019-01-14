# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    Name = models.CharField(max_length=250)
    Surname = models.CharField(max_length=250)
    Mail_or_Phone = models.CharField(max_length=20)
    Username = models.CharField(max_length=500)
    Password = models.CharField(max_length=250)
    Date_of_Birth = models.CharField(max_length=250)
    users = models.Manager()

    def __str__(self):
        return self.Name
