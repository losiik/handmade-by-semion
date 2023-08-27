from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import PageAbout


class PageAboutSerializer(ModelSerializer):
    class Meta:
        model = PageAbout
        fields = '__all__'
