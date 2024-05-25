from django.contrib.auth.views import LogoutView
from django.urls import path

from career.companies import views


app_name = 'companies'

urlpatterns = [
    path('register/', views.CompanyRegistrationView.as_view(), name='register-company'),
    path('login/', views.CompanyLoginView.as_view(), name='login-company'),
    path('company/<int:pk>/', views.CompanyDetailView.as_view(), name='company-detail')
]
