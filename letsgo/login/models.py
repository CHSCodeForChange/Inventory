from django.db import models
from django.contrib.auth.models import User
# class UserProfile(models.Model):
#     Description = models.CharField(max_length=200)
class Inventory(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null  = True,
        blank = True,
    )
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    

class InventoryItem(models.Model):
    parentInventory = models.ForeignKey(
        Inventory,
        on_delete=models.CASCADE,
        null  = True,
        blank = True,
    )
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
