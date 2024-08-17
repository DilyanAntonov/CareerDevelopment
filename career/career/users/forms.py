from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _

from career.companies.models import Company
from career.users.models import User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'stud_num', 'phone_number', 'profile_image']
        labels = {
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
            'email': _('Email Address'),
            'stud_num': _('Student Number'),
            'phone_number': _('Phone Number'),
            'profile_image': _('Profile Image'),
        }
        help_texts = {
            'first_name': _('Enter your first name'),
            'last_name': _('Enter your last name'),
            'email': _('Enter your email address'),
            'stud_num': _('Enter your student number'),
            'phone_number': _('Enter your phone number'),
            'profile_image': _('Upload your profile image'),
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'description', 'profile_image']
        labels = {
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
            'email': _('Email Address'),
            'phone_number': _('Phone Number'),
            'address': _('Address'),
            'description': _('Description'),
            'profile_image': _('Profile Image'),
        }
        help_texts = {
            'first_name': _('Enter your first name'),
            'last_name': _('Enter your last name'),
            'email': _('Enter your email address'),
            'phone_number': _('Enter your phone number'),
            'address': _('Enter your address'),
            'description': _('Enter a brief description about yourself'),
            'profile_image': _('Upload your profile image'),
        }

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['profile_image'].widget.attrs.update({'class': 'form-control-file'})



class CompanyUpdateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['email', 'phone_number', 'name', 'description', 'industry', 'location', 'website', 'contact_email',
                  'logo', 'established_year', 'eik']
        labels = {
            'email': _('Email Address'),
            'phone_number': _('Phone Number'),
            'name': _('Company Name'),
            'description': _('Description'),
            'industry': _('Industry'),
            'location': _('Location'),
            'website': _('Website'),
            'contact_email': _('Contact Email'),
            'logo': _('Company Logo'),
            'established_year': _('Established Year'),
            'eik': _('EIK'),
        }
        help_texts = {
            'email': _('Enter the company\'s email address'),
            'phone_number': _('Enter the company\'s phone number'),
            'name': _('Enter the name of the company'),
            'description': _('Enter a brief description of the company'),
            'industry': _('Enter the industry the company operates in'),
            'location': _('Enter the location of the company'),
            'website': _('Enter the company\'s website URL'),
            'contact_email': _('Enter the contact email address'),
            'logo': _('Upload the company\'s logo'),
            'established_year': _('Enter the year the company was established'),
            'eik': _('Enter the company\'s EIK (Unique Identification Code)'),
        }

