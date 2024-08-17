from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Resume, Skill, Project, Education

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, ButtonHolder, Submit, Div
from crispy_forms.bootstrap import InlineCheckboxes


class ResumeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields['projects'].queryset = Project.objects.filter(user=user)
            self.fields['educations'].queryset = Education.objects.filter(user=user)
            self.fields['skills'].queryset = Skill.objects.all()

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                'Summary and Experience',
                Field('summary', css_class='form-control'),
                Field('experience', css_class='form-control'),
            ),
            Fieldset(
                'Education',
                InlineCheckboxes('educations'),
            ),
            Fieldset(
                'Projects',
                InlineCheckboxes('projects'),
            ),
            Fieldset(
                'Skills',
                InlineCheckboxes('skills'),
            ),
            Fieldset(
                'Interests',
                Field('interests', css_class='form-control'),
            ),
            ButtonHolder(
                Submit('save', 'Save', css_class='btn btn-primary')
            )
        )

    class Meta:
        model = Resume
        fields = ['summary', 'educations', 'experience', 'projects', 'skills', 'interests']


class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                'Project Details',
                Field('title', css_class='form-control'),
                Field('description', css_class='form-control'),
                Field('technologies', css_class='form-control'),
                Field('link', css_class='form-control'),
            ),
            ButtonHolder(
                Submit('save', 'Save', css_class='btn btn-primary')
            )
        )

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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                'Education Details',
                Field('institution_name', css_class='form-control'),
                Field('course_name', css_class='form-control'),
                Div(
                    Div(Field('start_year', css_class='form-control'), css_class='col-md-6'),
                    Div(Field('end_year', css_class='form-control'), css_class='col-md-6'),
                    css_class='row'
                ),
                Field('certificate_link', css_class='form-control'),
            ),
            ButtonHolder(
                Submit('save', 'Save', css_class='btn btn-primary')
            )
        )

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
