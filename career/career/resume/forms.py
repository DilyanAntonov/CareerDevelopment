from django import forms
from .models import Resume, Skill, Project, Education


class ResumeForm(forms.ModelForm):
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    projects = forms.ModelMultipleChoiceField(
        queryset=Project.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    educations = forms.ModelMultipleChoiceField(
        queryset=Education.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Resume
        fields = ['summary', 'educations', 'experience', 'projects', 'skills', 'interests']

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


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['institution_name', 'course_name', 'start_year', 'end_year', 'certificate_link']
