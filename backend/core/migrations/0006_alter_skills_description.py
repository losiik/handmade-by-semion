# Generated by Django 4.2.4 on 2023-09-04 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_skills_description_tag_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='description',
            field=models.TextField(default='Text'),
        ),
    ]