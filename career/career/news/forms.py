from django import forms
from django.utils.translation import gettext_lazy as _

from .models import News

from django_ckeditor_5.widgets import CKEditor5Widget


class NewsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].required = False

    class Meta:
        model = News
        fields = ['title', 'content']
        labels = {
            'title': _('Title'),
            'content': _('Content'),
        }
        help_texts = {
            'title': _('Enter the title of the news article'),
            'content': _('Enter the content of the news article'),
        }
        widgets = {
            "content": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            )
        }
