from django.urls import include, path
from . import views


urlpatterns = [
    path('main_page/', views.PageAboutView.as_view())
]