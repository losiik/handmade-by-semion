from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import PageAbout, PageContacts, EmailMessage, SendEmailSettings, Skills, Tag


class PageAboutSerializer(ModelSerializer):
    class Meta:
        model = PageAbout
        fields = '__all__'


class PageContactsSerializer(ModelSerializer):
    class Meta:
        model = PageContacts
        fields = '__all__'


class SendEmailSettingsSerializer(ModelSerializer):
    class Meta:
        model = SendEmailSettings
        fields = '__all__'


class EmailMessageSerializer(ModelSerializer):
    class Meta:
        model = EmailMessage
        fields = '__all__'


class SkillsSerializer(ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'


class TagSerializer(ModelSerializer):
    def to_representation(self, instance):
        rep = super(TagSerializer, self).to_representation(instance)
        rep['skill'] = instance.skill.skill
        return rep

    class Meta:
        model = Tag
        fields = '__all__'
