from django.urls import path
from .views import (ResumeCreateView, ResumeDetailView, ProjectCreateView, ProjectListView, ProjectDeleteView,
                    EducationCreateView, EducationListView, EducationDeleteView, ResumeUpdateView, ProjectUpdateView)

app_name = 'resume'

urlpatterns = [
    path('resume/', ResumeDetailView.as_view(), name='resume-detail'),
    path('create-resume/', ResumeCreateView.as_view(), name='create-resume'),
    path('update-resume/', ResumeUpdateView.as_view(), name='update-resume'),
    path('projects/', ProjectListView.as_view(), name='projects-list'),
    path('create-project/', ProjectCreateView.as_view(), name='create-project'),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='update-project'),
    path('delete/<int:pk>/', ProjectDeleteView.as_view(), name='delete-project'),
    path('education/', EducationListView.as_view(), name='education-list'),
    path('create-education/', EducationCreateView.as_view(), name='create-education'),
    path('education/delete/<int:pk>/', EducationDeleteView.as_view(), name='delete-education'),
]
