from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=16)
    firstName = models.TextField()
    lastName = models.TextField()
    email = models.TextField()
    password = models.TextField()
    DateJoined = models.DateTimeField()

    def __str__(self):
        return self.username
