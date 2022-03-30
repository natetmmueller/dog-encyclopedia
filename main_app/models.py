from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Dog(models.Model):
    breed = models.CharField(max_length=200)
    description = models.TextField(max_length=250)
    activity = models.IntegerField()
    image = models.CharField(default=None, blank=True, null=True, max_length=255)
