from django.db import models
from career.users.models import BaseUser


class Company(BaseUser):
    name = models.CharField(max_length=255)
    description = models.TextField()
    employees_num = models.IntegerField(null=True, blank=True)
    industry = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    website = models.CharField(max_length=200, blank=True)
    contact_email = models.EmailField()
    logo = models.ImageField(upload_to='company_logos/', blank=True)
    established_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.is_company = True
        super().save(*args, **kwargs)
