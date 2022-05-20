from django.db import models

# Create your models here.
class cookrecipe(models.Model):
    recipe = models.CharField(max_length=100)
    ingredient = models.CharField(max_length=255)
    image_list = models.URLField(max_length=200, default ="")

