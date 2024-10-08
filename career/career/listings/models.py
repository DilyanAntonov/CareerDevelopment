from django.db import models
from django.utils.translation import gettext_lazy as _

from django_ckeditor_5.fields import CKEditor5Field

from career.companies.models import Company


class JobListing(models.Model):
    FULL_TIME = 'FT'
    PART_TIME = 'PT'
    CONTRACT = 'CT'
    TEMPORARY = 'TP'
    INTERN = 'IN'

    EMPLOYMENT_TYPE_CHOICES = [
        (FULL_TIME, _('Full-time')),
        (PART_TIME, _('Part-time')),
        (CONTRACT, _('Contract')),
        (TEMPORARY, _('Temporary')),
        (INTERN, _('Intern')),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = CKEditor5Field('Description', config_name='extends')
    requirements = models.TextField()
    location = models.CharField(max_length=255)
    employment_type = models.CharField(
        max_length=2,
        choices=EMPLOYMENT_TYPE_CHOICES,
        default=FULL_TIME,
    )
    posted_date = models.DateField(auto_now_add=True)
    salary_min = models.IntegerField(blank=True, null=True)
    salary_max = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
