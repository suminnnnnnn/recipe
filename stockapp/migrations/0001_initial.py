# Generated by Django 3.2.5 on 2022-05-23 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Add_stock', models.CharField(max_length=10, null=True)),
                ('Add_amount', models.CharField(max_length=4, null=True)),
                ('Add_month', models.DateField()),
            ],
            options={
                'db_table': 'Add',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_stock', models.CharField(max_length=10, null=True)),
                ('stock_amount', models.CharField(max_length=4, null=True)),
                ('stock_month', models.DateField()),
            ],
            options={
                'db_table': 'Stock',
            },
        ),
    ]