from django.urls import path
from .views import ResumeCreateView, ResumeDetailView, ProjectCreateView, ProjectListView, ProjectDeleteView

app_name = 'resume'

urlpatterns = [
    path('resume/', ResumeDetailView.as_view(), name='resume-detail'),
    path('create-resume/', ResumeCreateView.as_view(), name='create-resume'),
    path('projects/', ProjectListView.as_view(), name='projects-list'),
    path('create-project/', ProjectCreateView.as_view(), name='create-project'),
    path('delete/<int:pk>/', ProjectDeleteView.as_view(), name='delete-project'),
]
