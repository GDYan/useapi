from django.db import models

# Create your models here.

class myuser(models.Model):
    name = models.CharField(max_length=8)
    pwd = models.CharField(max_length=10)