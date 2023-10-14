from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import PageAbout, PageContacts, EmailMessage, SendEmailSettings, Skill, \
    WorkDirection, Projects


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


class WorkDirectionSerializer(ModelSerializer):
    class Meta:
        model = WorkDirection
        fields = '__all__'


class SkillSerializer(ModelSerializer):
    def to_representation(self, instance):
        rep = super(SkillSerializer, self).to_representation(instance)
        rep['work_direction'] = instance.work_direction.work_direction
        return rep

    class Meta:
        model = Skill
        fields = '__all__'


class ProjectsSerializer(ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'
