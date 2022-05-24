from django.db import models
from django.db.models.fields import CharField, URLField

# Create your models here.
class recipe(models.Model):
    recipe = models.CharField(max_length=255)
    ingredient = models.CharField(max_length=255)
    image = models.URLField(max_length=255, default ="")
    urls = models.URLField(max_length=255)

    class Meta:
        db_table = 'recipe'
        managed = False

