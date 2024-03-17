from django.db import models
from career.companies.models import Company


class JobListing(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    location = models.CharField(max_length=255)
    employment_type = models.CharField(max_length=50)
    posted_date = models.DateField(auto_now_add=True)
    application_deadline = models.DateField()
    salary_range = models.CharField(max_length=100, blank=True)
