from django.db import models

# Create your models here.
class User(models.Model):

    username = models.CharField(max_length=8),
    password = models.CharField(max_length=10)
class myuser(models.Model):
    name = models.CharField(max_length=8)
    pwd = models.CharField(max_length=10)