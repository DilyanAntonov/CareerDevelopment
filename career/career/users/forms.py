from django.contrib.auth.forms import UserCreationForm
from django import forms

from career.users.models import User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number']
