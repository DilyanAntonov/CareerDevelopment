from django.db import models
from career.users.models import BaseUser


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Education(models.Model):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    institution_name = models.CharField(max_length=255)
    course_name = models.CharField(max_length=255)
    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True, null=True)
    certificate_link = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.institution_name} - {self.course_name}"


class Project(models.Model):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=200, blank=True)
    link = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title


class Resume(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE)
    summary = models.TextField()
    education = models.TextField()
    experience = models.TextField()
    skills = models.ManyToManyField(Skill, blank=True)
    languages = models.ManyToManyField(Language, blank=True)
    projects = models.ManyToManyField(Project, blank=True)
    educations = models.ManyToManyField(Education, blank=True)
    interests = models.CharField(max_length=300, blank=True)
