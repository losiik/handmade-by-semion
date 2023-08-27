from django.contrib import admin

from .models import PageAbout


@admin.register(PageAbout)
class PageAboutAdmin(admin.ModelAdmin):
    pass
