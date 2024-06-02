from django.urls import path
from .views import ResumeCreateView, ResumesListView, ProjectCreateView, ProjectListView, ProjectDeleteView

app_name = 'resume'

urlpatterns = [
    path('resumes/', ResumesListView.as_view(), name='resume-list'),
    path('create-resume/', ResumeCreateView.as_view(), name='create-resume'),
    path('projects/', ProjectListView.as_view(), name='projects-list'),
    path('create-project/', ProjectCreateView.as_view(), name='create-project'),
    path('delete/<int:pk>/', ProjectDeleteView.as_view(), name='delete-project'),
]
