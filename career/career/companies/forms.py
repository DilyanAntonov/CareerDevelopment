from django.contrib.auth.forms import UserCreationForm
from .models import Company


class CompanyRegistrationForm(UserCreationForm):
    class Meta:
        model = Company
        fields = ('email', 'name', 'description', 'employees_num', 'industry', 'location', 'website', 'contact_email',
                  'logo', 'established_year', 'eik', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(CompanyRegistrationForm, self).__init__(*args, **kwargs)
        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None
