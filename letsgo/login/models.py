from django.db import models
from django.contrib.auth.models import User
class UserProfile(models.Model):
    Description = models.CharField(max_length=200)
