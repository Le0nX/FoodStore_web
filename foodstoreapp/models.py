from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class FoodStore(models.Model):
    # One owner of a FoodStore. So we are using OneToOneField...
    # models.CASCADE means that deleting user we delete all data too
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='foodstore')
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='foodstore_logo/', blank=False)

    def __str__(self):      # feature for admin pannel - indexes by name
        return self.name
