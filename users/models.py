from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    """
    The new default user model.
    """
    age = models.PositiveIntegerField(null=True, blank=True)
