# Generated by Django 3.2.5 on 2022-05-23 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cookrecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.CharField(max_length=100)),
                ('ingredient', models.CharField(max_length=255)),
                ('image_list', models.URLField(default='')),
            ],
        ),
    ]
