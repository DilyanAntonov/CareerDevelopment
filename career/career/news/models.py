from django.db import models
from career.companies.models import Company
from django_ckeditor_5.fields import CKEditor5Field


class News(models.Model):
    title = models.CharField(max_length=255)
    date_posted = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='news_articles')
    content = CKEditor5Field('Content', config_name='extends')

    def __str__(self):
        return self.title
