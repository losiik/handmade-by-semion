from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PageAbout
from core.serializers import PageAboutSerializer


class PageAboutView(APIView):
    queryset = PageAbout.objects.all()
    serializer_class = PageAboutSerializer

    def get(self, request):
        main_page = PageAbout.objects.all()
        serializer = PageAboutSerializer(main_page, many=True)
        return Response({"about": serializer.data})
