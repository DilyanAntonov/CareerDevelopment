from django import forms
from .models import Resume, Skill, Project, Education


class ResumeForm(forms.ModelForm):
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    projects = forms.ModelMultipleChoiceField(
        queryset=Project.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    educations = forms.ModelMultipleChoiceField(
        queryset=Education.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Resume
        fields = ['summary', 'educations', 'experience', 'projects', 'skills', 'interests']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'technologies', 'link']


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['institution_name', 'course_name', 'start_year', 'end_year', 'certificate_link']
