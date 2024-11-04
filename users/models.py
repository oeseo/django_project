from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255)
    position = models.ForeignKey('Position', on_delete=models.SET_NULL, null=True, blank=True)
    dismissed = models.BooleanField(default=False)
    dismissal_date = models.DateField(null=True, blank=True)
    objects = UserManager()

    def __str__(self):
        return self.username
