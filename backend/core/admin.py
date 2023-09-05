from django.contrib import admin

from .models import PageAbout, PageContacts, SendEmailSettings, EmailMessage, Skills, Tag, CertificatesImage


class CertificatesImageAdmin(admin.StackedInline):
    model = CertificatesImage


@admin.register(PageAbout)
class PageAboutAdmin(admin.ModelAdmin):
    inlines = [CertificatesImageAdmin]

    class Meta:
        model = PageAbout


@admin.register(CertificatesImage)
class CertificatesImage(admin.ModelAdmin):
    pass

@admin.register(PageContacts)
class PageContactsAdmin(admin.ModelAdmin):
    pass


@admin.register(SendEmailSettings)
class SendEmailSettingsAdmin(admin.ModelAdmin):
    pass


@admin.register(EmailMessage)
class EmailMessageAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
