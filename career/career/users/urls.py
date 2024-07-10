from django.contrib.auth.views import LogoutView
from django.urls import path

from career.users import views
from django.contrib.auth import views as auth_views


app_name = 'users'

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration-success/', views.RegistrationSuccessView.as_view(), name='registration-success'),
    path('user/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('profile/update/', views.UserUpdateView.as_view(), name='user-update'),
    path('password_change/', views.CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
         name='password_change_done'),
]
