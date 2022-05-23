# Generated by Django 3.2.5 on 2022-05-23 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.CharField(max_length=255)),
                ('ingredient', models.CharField(max_length=255)),
                ('image', models.URLField(default='')),
            ],
        ),
        migrations.DeleteModel(
            name='cookrecipe',
        ),
    ]