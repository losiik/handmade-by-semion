from django.urls import include, path
from . import views


urlpatterns = [
    path('main_page/', views.PageAboutView.as_view()),
    path('contacts_page/', views.PageContactsView.as_view()),
    path('send_email_setings/', views.SendEmailSettingsView.as_view()),
    path('send_email/', views.EmailMessageView.as_view()),
    path('get_filter/', views.GetFiltersView.as_view()),
    path('get_all_work_dir/', views.GetAllWorkDirView.as_view()),
    path('get_full_work_dir_info/', views.GetFullWorkDirInfoView.as_view()),
    path('get_all_projects/', views.GetAllProjectsView.as_view()),
    path('get_full_project_info/', views.GetFullProjectInfoView.as_view()),
    path('get_projects_by_skill/', views.GetProjectsBySkill.as_view()),
]
