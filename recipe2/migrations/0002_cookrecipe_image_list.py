# Generated by Django 3.2.5 on 2022-05-20 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cookrecipe',
            name='image_list',
            field=models.URLField(default=''),
        ),
    ]
