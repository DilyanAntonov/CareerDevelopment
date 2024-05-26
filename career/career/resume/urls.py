from django.urls import path
from .views import ResumeCreateView, ResumesListView

app_name = 'resume'

urlpatterns = [
    path('resumes/', ResumesListView.as_view(), name='resume-list'),
    path('create-resume/', ResumeCreateView.as_view(), name='create-resume'),
]
