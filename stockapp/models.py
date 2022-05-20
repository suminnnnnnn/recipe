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
    Add_stock = CharField(max_length=10, null=True)
    Add_amount = CharField(max_length=4, null=True)
    Add_month = CharField(max_length=20, null=True)

    class Meta:
        db_table = 'Add'
        app_label = 'stockapp'

class stock(models.Model):
  stock_name = CharField(max_length=10)
  stock_amount = CharField(max_length=20)
  distance = FloatField()
  time_info = CharField(max_length=10)
  start_end_info = CharField(max_length=30)
  cre_date = DateField()
  class Meta:
    db_table = 'stock'
    # managed = False

