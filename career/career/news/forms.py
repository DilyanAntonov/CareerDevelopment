from django import forms
from django.utils.translation import gettext_lazy as _

from .models import News


class NewsForm(forms.ModelForm):
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
