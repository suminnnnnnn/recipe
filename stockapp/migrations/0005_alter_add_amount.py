# Generated by Django 3.2.5 on 2022-05-19 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0004_alter_add_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add',
            name='amount',
            field=models.IntegerField(),
        ),
    ]
