# Generated by Django 4.2.3 on 2023-10-23 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PageAbout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField()),
                ('photo', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name_plural': 'About settings',
            },
        ),
        migrations.CreateModel(
            name='PageContacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Contacts settings',
            },
        ),
        migrations.CreateModel(
            name='PrivacyPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.FileField(upload_to='files/documents/privacy_policy')),
            ],
            options={
                'verbose_name_plural': 'Privacy policy file',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(default='max project_name length is 300 characters', max_length=300)),
                ('preview_description', models.TextField()),
                ('full_description', models.TextField()),
                ('head_photo', models.FileField(upload_to='')),
                ('slug', models.SlugField(blank=True, default=None, max_length=255)),
                ('meta_keywords', models.TextField(blank=True, default=None)),
                ('meta_title', models.CharField(blank=True, default=None, max_length=50)),
                ('meta_description', models.CharField(blank=True, default=None, max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Projects settings',
            },
        ),
        migrations.CreateModel(
            name='SendEmailSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=255)),
                ('port', models.CharField(max_length=255)),
                ('email_address_from', models.CharField(max_length=255)),
                ('email_password', models.CharField(max_length=255)),
                ('email_address_to', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Email settings',
            },
        ),
        migrations.CreateModel(
            name='WorkDirection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_direction', models.CharField(max_length=255)),
                ('description', models.TextField(default=None)),
                ('slug', models.SlugField(blank=True, default=None, max_length=255)),
                ('meta_keywords', models.TextField(blank=True, default=None)),
                ('meta_title', models.CharField(blank=True, default=None, max_length=50)),
                ('meta_description', models.CharField(blank=True, default=None, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=255)),
                ('description', models.TextField(default=None)),
                ('slug', models.SlugField(blank=True, default=None, max_length=255)),
                ('work_direction', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.workdirection')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_photo', models.FileField(upload_to='projects/')),
                ('project', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.projects')),
            ],
        ),
        migrations.AddField(
            model_name='projects',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.skill'),
        ),
        migrations.CreateModel(
            name='CertificatesImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificates', models.FileField(upload_to='certificates/')),
                ('about', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.pageabout')),
            ],
        ),
    ]
