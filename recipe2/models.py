from django.db import models

# Create your models here.
class cookrecipe(models.Model):
    name = models.CharField(max_length=255)
    ingredient = models.CharField(max_length=255)
