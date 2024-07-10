from django.urls import path
from django.contrib.auth import views as auth_views

from career.companies import views


app_name = 'companies'

urlpatterns = [
    path('register/', views.CompanyRegistrationView.as_view(), name='register-company'),
    path('login/', views.CompanyLoginView.as_view(), name='login-company'),
    path('company/<int:pk>/', views.CompanyDetailView.as_view(), name='company-detail'),
    path('profile/update/', views.CompanyUpdateView.as_view(), name='company-update'),
    path('password_change/', views.CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='companies/password_change_done.html'),
         name='password_change_done'),
    path('manage-job-listings/<int:pk>/', views.ManageJobListingsView.as_view(), name='manage-job-listings'),
    path('edit-job-listing/<int:pk>/', views.JobListingUpdateView.as_view(), name='edit-job-listing'),
    path('delete-job-listing/<int:pk>/', views.JobListingDeleteView.as_view(), name='delete-job-listing'),
]
