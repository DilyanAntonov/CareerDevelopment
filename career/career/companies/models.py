from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    industry = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    website = models.URLField(max_length=200, blank=True)
    contact_email = models.EmailField()
    logo = models.ImageField(upload_to='company_logos/', blank=True)
    established_year = models.IntegerField(null=True, blank=True)
