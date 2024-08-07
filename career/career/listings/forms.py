from django import forms
from django.utils.translation import gettext_lazy as _

from .models import JobListing


class JobListingForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = [
            'title', 'description', 'requirements',
            'location', 'employment_type', 'salary_min', 'salary_max'
        ]
        labels = {
            'title': _('Job Title'),
            'description': _('Job Description'),
            'requirements': _('Job Requirements'),
            'location': _('Location'),
            'employment_type': _('Employment Type'),
            'salary_min': _('Minimum Salary'),
            'salary_max': _('Maximum Salary'),
        }
        help_texts = {
            'title': _('Enter the title of the job'),
            'description': _('Enter a detailed description of the job'),
            'requirements': _('Enter the requirements for the job'),
            'location': _('Enter the location of the job'),
            'employment_type': _('Select the type of employment'),
            'salary_min': _('Enter the minimum salary for this job'),
            'salary_max': _('Enter the maximum salary for this job'),
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
            'requirements': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
            'employment_type': forms.Select(choices=JobListing.EMPLOYMENT_TYPE_CHOICES),
        }
