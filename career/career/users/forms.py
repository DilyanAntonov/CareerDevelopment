from django.contrib.auth.forms import UserCreationForm
from django import forms

from career.companies.models import Company
from career.users.models import User, BaseUser


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'description', 'image']

class CompanyUpdateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'name', 'description', 'industry', 'location', 'website', 'contact_email', 'logo', 'established_year']