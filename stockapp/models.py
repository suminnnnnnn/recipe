from operator import mod
from pickle import TRUE
from django.db import models
from django.db.models.fields import CharField, IntegerField, FloatField
from django.db.models.fields import DateField
# from ingredient.models import Ingredient
from django.contrib.auth.models import User



class Add(models.Model):
    #user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    #user_name = models.CharField(max_length=10, null=True)
    Add_stock = CharField(max_length=10, null=True)
    Add_amount = CharField(max_length=4, null=True)
    Add_month = DateField()

    class Meta:
        db_table = 'Add'
        app_label = 'stockapp'

class Stock(models.Model):
    stock_stock = models.CharField(max_length=10, null=True)
    stock_amount = models.CharField(max_length=4, null=True)
    stock_month = DateField()
    class Meta:
      db_table = 'Stock'
      app_label = 'stockapp'
    # managed = False

