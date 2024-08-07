from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from .models import Company


class CompanyRegistrationForm(UserCreationForm):
    class Meta:
        model = Company
        fields = ('email', 'name', 'description', 'employees_num', 'industry', 'location', 'website', 'contact_email',
                  'logo', 'established_year', 'eik', 'password1', 'password2')
        labels = {
            'email': _('Email Address'),
            'name': _('Company Name'),
            'description': _('Description'),
            'employees_num': _('Number of Employees'),
            'industry': _('Industry'),
            'location': _('Location'),
            'website': _('Website'),
            'contact_email': _('Contact Email'),
            'logo': _('Company Logo'),
            'established_year': _('Established Year'),
            'eik': _('EIK'),
            'password1': _('Password'),
            'password2': _('Confirm Password'),
        }
        help_texts = {
            'email': _('Enter the company\'s email address'),
            'name': _('Enter the name of the company'),
            'description': _('Enter a brief description of the company'),
            'employees_num': _('Enter the number of employees in the company'),
            'industry': _('Enter the industry the company operates in'),
            'location': _('Enter the location of the company'),
            'website': _('Enter the company\'s website URL'),
            'contact_email': _('Enter the contact email address'),
            'logo': _('Upload the company\'s logo'),
            'established_year': _('Enter the year the company was established'),
            'eik': _('Enter the company\'s EIK (Unique Identification Code)'),
            'password1': _('Enter a password for the account'),
            'password2': _('Re-enter the password for confirmation'),
        }

    def __init__(self, *args, **kwargs):
        super(CompanyRegistrationForm, self).__init__(*args, **kwargs)
        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None
