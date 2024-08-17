from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class BaseUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True, blank=True)
    phone_number = models.CharField(help_text=_('(country code) digits'), max_length=17, null=True)
    is_company = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super(BaseUser, self).save(*args, **kwargs)


class User(BaseUser):
    address = models.CharField(max_length=150, null=True)
    description = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images', blank=True,
                                      default='profile_images/default_profile_image.png')
    stud_num = models.CharField(max_length=10)
