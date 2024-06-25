from django.db import models
from career.users.models import BaseUser
from career.listings.models import JobListing
from career.resume.models import Resume


class Application(models.Model):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    application_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50)
    cover_letter = models.TextField(blank=True)
    resume = models.ForeignKey(Resume, on_delete=models.SET_NULL, null=True, blank=True)
