from django.db import models


class PageAbout(models.Model):
    about = models.TextField()
    photo = models.FileField()
    certificates = models.FileField()

    def __str__(self):
        name_object = 'About settings'
        return name_object

    class Meta:
        verbose_name_plural = 'About settings'


class PrivacyPolicy(models.Model):
    content = models.FileField()

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


class Tag(models.Model):
    tag = models.CharField(max_length=255)

    def __str__(self):
        return self.tag


class Projects(models.Model):
    title = models.CharField(max_length=300, default='max title length is 300 characters')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    small_description = models.TextField()
    full_description = models.TextField()
    head_photo = models.FileField()
    additional_photos = models.FileField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Projects settings'
