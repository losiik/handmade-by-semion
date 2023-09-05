from django.forms import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PageAbout, PageContacts, SendEmailSettings, Skills, Tag, CertificatesImage
from .send_mail import SendMail
from .serializers import PageAboutSerializer, PageContactsSerializer, SendEmailSettingsSerializer, \
    EmailMessageSerializer, SkillsSerializer, TagSerializer


class PageAboutView(APIView):
    queryset = PageAbout.objects.all()
    serializer_class = PageAboutSerializer

    @csrf_exempt
    def get(self, request):
        certificates = []
        main_page = PageAbout.objects.all()
        serializer = PageAboutSerializer(main_page, many=True)
        certificates_data = CertificatesImage.objects.all()

        for certificate_data in certificates_data:
            certificates.append(certificate_data.certificates.path)

        return Response({"about": serializer.data, "certificates": certificates})


class PageContactsView(APIView):
    queryset = PageContacts.objects.all()
    serializer_class = PageContactsSerializer

    @csrf_exempt
    def get(self, request):
        contacts_page = PageContacts.objects.all()
        serializer = PageContactsSerializer(contacts_page, many=True)
        return Response({"contacts": serializer.data})


class SendEmailSettingsView(APIView):
    queryset = SendEmailSettings.objects.all()
    serializer_class = SendEmailSettingsSerializer


class EmailMessageView(APIView):
    serializer_class = EmailMessageSerializer

    @csrf_exempt
    def post(self, request):
        queryset_email_cred = SendEmailSettings.objects.all()
        email_creds = model_to_dict(queryset_email_cred[0])

        message = request.data['message']
        send_mail = SendMail(host=email_creds['host'],
                             port=email_creds['port'],
                             email_address_from=email_creds['email_address_from'],
                             email_password=email_creds['email_password'],
                             email_address_to=email_creds['email_address_to'],
                             message=message)

        return Response({"Send email success": send_mail.send_email()})


class SkillsView(APIView):
    queryset = PageContacts.objects.all()
    serializer_class = PageContactsSerializer

    @csrf_exempt
    def get(self, request):
        skills = Skills.objects.all()
        serializer = SkillsSerializer(skills, many=True)
        return Response({"skills": serializer.data})


class GetAllTagsView(APIView):
    @csrf_exempt
    def get(self, request):
        response = {}

        skills = Skills.objects.all()
        skills_serializer = SkillsSerializer(skills, many=True)

        for skill in skills_serializer.data:
            tags = Tag.objects.filter(skill=skill['id'])
            tags_serializer = TagSerializer(tags, many=True)
            response[skill['skill']] = []
            for tag in tags_serializer.data:
                response[skill['skill']].append(
                    {
                        'id': tag['id'],
                        'tag': tag['tag']
                    }
                )

        return Response({"all_tags": response})


class TagView(APIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class GetSkillFullInfo(APIView):
    @csrf_exempt
    def get(self, request):
        skill = request.query_params.get('skill')
        skill = Skills.objects.filter(skill=skill)
        skills_serializer = SkillsSerializer(skill, many=True)
        skill_data = skills_serializer.data

        tags = Tag.objects.filter(skill=skill_data[0]['id'])
        tags_serializer = TagSerializer(tags, many=True)

        response = {
            'skill': skill_data[0]['skill'],
            'description': skill_data[0]['description'],
            'tags': tags_serializer.data,
        }

        return Response({'skil': response})


