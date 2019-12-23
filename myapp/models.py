from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Dummy(models.Model):
    header = models.CharField(max_length=64, default="Header")
    text = models.TextField(default='Veniam eiusmod irure est aliqua aliqua aliqua \
        minim ut sit incididunt enim sit exercitation proident.')

class UserProfile(models.Model):
    age = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
