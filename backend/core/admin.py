from django.contrib import admin

from .models import (PageAbout, PageContacts, SendEmailSettings, EmailMessage, Skill,
                     WorkDirection, CertificatesImage, ProjectsImage, Projects)


class CertificatesImageAdmin(admin.StackedInline):
    model = CertificatesImage


@admin.register(PageAbout)
class PageAboutAdmin(admin.ModelAdmin):
    inlines = [CertificatesImageAdmin]

    class Meta:
        model = PageAbout


@admin.register(CertificatesImage)
class CertificatesImage(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


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


@admin.register(Skill)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ['skill', 'work_direction']


@admin.register(WorkDirection)
class WorkDirectionAdmin(admin.ModelAdmin):
    pass


class ProjectsImageAdmin(admin.StackedInline):
    model = ProjectsImage


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    inlines = [ProjectsImageAdmin]
    list_display = ['project_name', 'skill']

    class Meta:
        model = PageAbout


@admin.register(ProjectsImage)
class ProjectsImage(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}
