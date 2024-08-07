from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Resume, Skill, Project, Education


class ResumeForm(forms.ModelForm):
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label=_('Skills'),
        help_text=_('Select the skills relevant to the resume')
    )

    projects = forms.ModelMultipleChoiceField(
        queryset=Project.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label=_('Projects'),
        help_text=_('Select the projects to include in the resume')
    )

    educations = forms.ModelMultipleChoiceField(
        queryset=Education.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label=_('Educations'),
        help_text=_('Select the educations to include in the resume')
    )

    class Meta:
        model = Resume
        fields = ['summary', 'educations', 'experience', 'projects', 'skills', 'interests']
        labels = {
            'summary': _('Summary'),
            'experience': _('Experience'),
            'interests': _('Interests'),
        }
        help_texts = {
            'summary': _('Enter a brief summary of your professional background'),
            'experience': _('Detail your professional experience'),
            'interests': _('List your interests'),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields['projects'].queryset = Project.objects.filter(user=user)
            self.fields['educations'].queryset = Education.objects.filter(user=user)


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'technologies', 'link']
        labels = {
            'title': _('Project Title'),
            'description': _('Project Description'),
            'technologies': _('Technologies Used'),
            'link': _('Project Link'),
        }
        help_texts = {
            'title': _('Enter the title of the project'),
            'description': _('Enter a detailed description of the project'),
            'technologies': _('List the technologies used in the project'),
            'link': _('Enter a link to the project (if available)'),
        }


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['institution_name', 'course_name', 'start_year', 'end_year', 'certificate_link']
        labels = {
            'institution_name': _('Institution Name'),
            'course_name': _('Course Name'),
            'start_year': _('Start Year'),
            'end_year': _('End Year'),
            'certificate_link': _('Certificate Link'),
        }
        help_texts = {
            'institution_name': _('Enter the name of the institution'),
            'course_name': _('Enter the name of the course'),
            'start_year': _('Enter the year you started the course'),
            'end_year': _('Enter the year you completed the course (or expected completion year)'),
            'certificate_link': _('Enter a link to the certificate (if available)'),
        }
