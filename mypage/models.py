from django.db import models
from django.db import models
from django.db.models.fields import CharField, IntegerField,DateField
class Stock(models.Model):
        id = IntegerField(primary_key=True)
        stock_stock = CharField(max_length=10, null=True)
        stock_amount = CharField(max_length=4, null=True)
        stock_month = DateField()
        
        class Meta:
            db_table = 'Stock'
            app_label = 'mypage'
            managed = False