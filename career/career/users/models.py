from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), unique=True, blank=True)
    phone_number = models.CharField(help_text=_('(country code) digits'), max_length=17, null=True)
    address = models.CharField(max_length=150, null=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_images', blank=True)
