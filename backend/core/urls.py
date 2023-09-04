from django.urls import include, path
from . import views


urlpatterns = [
    path('main_page/', views.PageAboutView.as_view()),
    path('contacts_page/', views.PageContactsView.as_view()),
    path('send_email_setings/', views.SendEmailSettingsView.as_view()),
    path('send_email/', views.EmailMessageView.as_view()),
    path('all_skills/', views.SkillsView.as_view()),
    path('all_tags/', views.GetAllTags.as_view())
]
