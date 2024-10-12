from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Account(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True)
