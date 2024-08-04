from django.contrib.auth.forms import UserCreationForm
from django import forms

from career.companies.models import Company
from career.users.models import User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'stud_num', 'phone_number', "profile_image"]


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'description', 'profile_image']


class CompanyUpdateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['email', 'phone_number', 'name', 'description', 'industry', 'location', 'website', 'contact_email',
                  'logo', 'established_year', 'eik']
