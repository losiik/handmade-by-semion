# Generated by Django 4.2.3 on 2023-10-14 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workdirection',
            name='slug',
            field=models.SlugField(default=None),
        ),
        migrations.AlterField(
            model_name='skill',
            name='slug',
            field=models.SlugField(default=None),
        ),
    ]