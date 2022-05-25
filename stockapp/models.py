from distutils.text_file import TextFile
from operator import mod
from pickle import TRUE
from django.db import models
from django.db.models.fields import CharField, IntegerField, FloatField
from django.db.models.fields import DateField
# from ingredient.models import Ingredient
from django.contrib.auth.models import User

from member.models import Member



class Add(models.Model):
  
    Add_user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Add_username = CharField(max_length=10, null=True)
    # user_name = models.CharField(max_length=10, null=True)
    Add_stock = CharField(max_length=10, null=True)
    Add_amount = CharField(max_length=4, null=True)
    Add_month = DateField()

    class Meta:
        db_table = 'Add'
        app_label = 'stockapp'

class Stock(models.Model):

    stock_user = models.ForeignKey(User, on_delete=models.CASCADE,db_column='user_user_id')
    stock_stock = models.CharField(max_length=10, null=True)
    stock_amount = models.CharField(max_length=4, null=True)
    stock_month = DateField()
    stock_urls = models.URLField(max_length=255)
    class Meta:
      db_table = 'Stock'
      app_label = 'stockapp'
    # managed = False

