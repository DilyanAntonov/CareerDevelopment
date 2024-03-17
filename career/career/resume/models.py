from django.db import models
from career.users.models import User


class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    summary = models.TextField()
    education = models.TextField()
    experience = models.TextField()
    skills = models.CharField(max_length=500)
    certifications = models.CharField(max_length=500, blank=True)
    interests = models.CharField(max_length=300, blank=True)
