from django.forms import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import (PageAbout, PageContacts, Projects, SendEmailSettings, Skill,
                     CertificatesImage, ProjectsImage)
from .send_mail import SendMail
from .serializers import PageAboutSerializer, PageContactsSerializer, SendEmailSettingsSerializer, \
    EmailMessageSerializer, WorkDirection


class PageAboutView(APIView):
    queryset = PageAbout.objects.all()
    serializer_class = PageAboutSerializer

    @csrf_exempt
    def get(self, request):
        certificates = []
        main_page = PageAbout.objects.all()

        if not main_page:
            return Response(
                {"about": [{"about": "", "photo": ""}], "certificates": []}
            )
        main_page = main_page[0]
        certificates_data = CertificatesImage.objects.all()

        for certificate_data in certificates_data:
            certificates.append(certificate_data.certificates.path.replace('/app', ''))

        return Response(
            {"about": [
                {
                    "about": main_page.about,
                    "photo": main_page.photo.file.name.replace('/app', '')
                }
            ], "certificates": certificates}
        )


class PageContactsView(APIView):
    queryset = PageContacts.objects.all()
    serializer_class = PageContactsSerializer

    @csrf_exempt
    def get(self, request):
        contacts_page = PageContacts.objects.all()
        if not contacts_page:
            return Response(
                {"contacts": [
                    {
                        "phone": "",
                        "email": ""
                    }

                ]
                }
            )
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
        work_direction = request.data['work_direction']

        send_mail = SendMail(host=email_creds['host'],
                             port=email_creds['port'],
                             email_address_from=email_creds['email_address_from'],
                             email_password=email_creds['email_password'],
                             email_address_to=email_creds['email_address_to'],
                             message=message,
                             work_direction=work_direction)

        return Response({"Send email success": send_mail.send_email()})


class GetFiltersView(APIView):
    @csrf_exempt
    def get(self, request):
        response = {'all_skills': []}
        skills = Skill.objects.all().order_by('work_direction')

        for skill in skills:
            response['all_skills'].append({'skill': skill.skill, 'slug': skill.slug})
        return Response(response)


class GetAllWorkDirView(APIView):
    @csrf_exempt
    def get(self, request):
        response = {'all_work_dir': []}
        work_dirs = WorkDirection.objects.all().order_by('work_direction')

        for work_dir in work_dirs:
            response['all_work_dir'].append(
                {
                    'name': work_dir.work_direction,
                    'slug': work_dir.slug
                }
            )
        return Response(response)


class GetFullWorkDirInfoView(APIView):
    @csrf_exempt
    def get(self, request):
        slug = request.query_params.get('slug')
        response = {}

        work_dir = WorkDirection.objects.filter(slug=slug)[0]

        response['work_dir'] = work_dir.work_direction
        response['description'] = work_dir.description
        response['skills'] = []
        response['meta_keywords'] = work_dir.meta_keywords
        response['meta_title'] = work_dir.meta_title
        response['meta_description'] = work_dir.meta_description

        skills = Skill.objects.filter(work_direction=work_dir.id)

        for skill in skills:
            response['skills'].append(
                {'skill_name': skill.skill, 'skill_description': skill.description}
            )

        return Response(response)


class GetAllProjectsView(APIView):
    @csrf_exempt
    def get(self, request):
        response = {}
        response['selected_skill'] = ''
        response['projects'] = []

        projects = Projects.objects.all()

        for project in projects:
            response['projects'].append(
                {
                    'project_name': project.project_name,
                    'preview_description': project.preview_description,
                    'head_photo': project.head_photo.file.name.replace('/app', ''),
                    'slug': project.slug
                }
            )

        return Response(response)


class GetFullProjectInfoView(APIView):
    @csrf_exempt
    def get(self, request):
        slug = request.query_params.get('slug')
        response = {}
        project = Projects.objects.filter(slug=slug)[0]

        response['project_name'] = project.project_name
        response['slug'] = project.slug
        response['full_description'] = project.full_description
        response['photos'] = []
        response['meta_keywords'] = project.meta_keywords
        response['meta_title'] = project.meta_title
        response['meta_description'] = project.meta_description

        projects_imgs = ProjectsImage.objects.filter(project=project.id)
        for img in projects_imgs:
            response['photos'].append(img.project_photo.file.name.replace('/app', ''))

        return Response(response)


class GetProjectsBySkill(APIView):
    @csrf_exempt
    def get(self, request):
        skill_slug = request.query_params.get('skill_slug')
        response = {}

        skill = Skill.objects.filter(slug=skill_slug)[0]
        response['selected_skill'] = skill.skill

        projects = Projects.objects.filter(skill=skill.id)
        response['projects'] = []

        for project in projects:
            response['projects'].append(
                {
                    'project_name': project.project_name,
                    'preview_description': project.preview_description,
                    'head_photo': project.head_photo.file.name.replace('/app', ''),
                    'slug': project.slug,
                    'meta_keywords': project.meta_keywords,
                    'meta_title': project.meta_title,
                    'meta_description': project.meta_description
                }
            )

        return Response(response)
