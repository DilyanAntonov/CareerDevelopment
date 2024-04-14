from django.urls import path

from career.users import views


app_name = 'users'

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('registration-success/', views.RegistrationSuccessView.as_view(), name='registration-success'),
]
