from django import forms
from .models import JobListing


class JobListingForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = [
            'company', 'title', 'description', 'requirements',
            'location', 'employment_type', 'application_deadline', 'salary_range'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
            'requirements': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
            'application_deadline': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }