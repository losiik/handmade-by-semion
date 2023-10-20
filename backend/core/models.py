from django.db import models
from django.template.defaultfilters import slugify


class PageAbout(models.Model):
    about = models.TextField()
    photo = models.FileField()

    def __str__(self):
        name_object = 'About settings'
        return name_object

    class Meta:
        verbose_name_plural = 'About settings'


class CertificatesImage(models.Model):
    about = models.ForeignKey(PageAbout, default=None, on_delete=models.CASCADE)
    certificates = models.FileField(upload_to='certificates/')


class PrivacyPolicy(models.Model):
    content = models.FileField(upload_to='files/documents/privacy_policy')

    def __str__(self):
        name_object = 'Privacy policy file'
        return name_object

    class Meta:
        verbose_name_plural = 'Privacy policy file'


class SendEmailSettings(models.Model):
    host = models.CharField(max_length=255)
    port = models.CharField(max_length=255)
    email_address_from = models.CharField(max_length=255)
    email_password = models.CharField(max_length=255)
    email_address_to = models.CharField(max_length=255)

    def __str__(self):
        name_object = 'Email settings'
        return name_object

    class Meta:
        verbose_name_plural = 'Email settings'


class EmailMessage(models.Model):
    message = models.TextField()


class PageContacts(models.Model):
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        name_object = 'Contacts settings'
        return name_object

    class Meta:
        verbose_name_plural = 'Contacts settings'


class WorkDirection(models.Model):
    work_direction = models.CharField(max_length=255)
    description = models.TextField(default=None)
    slug = models.SlugField(default=None, blank=True, max_length=255)

    # seo meta
    # meta_keywords = models.TextField(blank=True, default=None) # скилы через запятую
    # meta_title = models.CharField(max_length=50) # синоним к work_direction
    # meta_description = models.CharField(max_length=150) # синоним к work_direction

    def save(self, *args, **kwargs):
        self.slug = slugify(self.work_direction)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.work_direction


class Skill(models.Model):
    work_direction = models.ForeignKey(WorkDirection, on_delete=models.CASCADE, default=None)
    skill = models.CharField(max_length=255)
    description = models.TextField(default=None)
    slug = models.SlugField(default=None, blank=True, max_length=255)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.skill)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.skill


class Projects(models.Model):
    project_name = models.CharField(max_length=300, default='max project_name length is 300 characters')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    preview_description = models.TextField()
    full_description = models.TextField()
    head_photo = models.FileField()
    slug = models.SlugField(default=None, blank=True, max_length=255)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.project_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name_plural = 'Projects settings'


class ProjectsImage(models.Model):
    project = models.ForeignKey(Projects, default=None, on_delete=models.CASCADE)
    project_photo = models.FileField(upload_to='projects/')
