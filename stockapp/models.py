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
  
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # user_name = models.CharField(max_length=10, null=True)
    Add_stock = CharField(max_length=10, null=True)
    Add_amount = CharField(max_length=4, null=True)
    Add_month = DateField()

    class Meta:
        db_table = 'Add'
        app_label = 'stockapp'

class Stock(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_user_id')
    stock_stock = models.CharField(max_length=10, null=True)
    stock_amount = models.CharField(max_length=4, null=True)
    stock_month = DateField()
    stock_urls = models.URLField(max_length=255)
    class Meta:
      db_table = 'Stock'
      app_label = 'stockapp'
    # managed = False

# class Url(models.Model):
#     url_stock = models.TextField()
#     url_start = models.TextField()
#     url_end = models.TextField()
#     url_all = models.TextField()
#     url_list = models.TextField()
#     class Meta:
#       db_table = 'Url'
#       app_label = 'stockapp'
#     # managed = False

