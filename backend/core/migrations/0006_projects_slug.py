# Generated by Django 4.2.3 on 2023-10-14 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_title_projects_project_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='slug',
            field=models.SlugField(blank=True, default=None),
        ),
    ]