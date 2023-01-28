from django.contrib.auth.models import AbstractUser

# from django.db import models

# Create your models here.


class User(AbstractUser):
    pass

    # para que el usuario acceda solo con su email
    # email = models.EmailField(unique=True)

    # USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = []
