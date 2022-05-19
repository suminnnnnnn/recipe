from operator import mod
from django.db import models
from django.db.models.fields import CharField, IntegerField, FloatField
from django.db.models.fields import DateField
# from ingredient.models import Ingredient
from django.contrib.auth.models import User



class Add(models.Model):
    #user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    #user_name = models.CharField(max_length=10, null=True)
    stock = models.CharField(max_length=10, null=True)
    #expiration_date = models.DateField(auto_now_add=True)
    amount = models.IntegerField()

    class Meta:
        db_table = 'Add'
        app_label = 'stockapp'
