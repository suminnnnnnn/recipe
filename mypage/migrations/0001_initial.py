# Generated by Django 3.2.5 on 2022-05-24 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('stock_stock', models.CharField(max_length=10, null=True)),
                ('stock_amount', models.CharField(max_length=4, null=True)),
                ('stock_month', models.DateField()),
            ],
            options={
                'db_table': 'Stock',
                'managed': False,
            },
        ),
    ]
