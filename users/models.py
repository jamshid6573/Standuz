from email.policy import default
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import AbstractUser


class UsersAb(AbstractUser):
    gold = models.FloatField(default=0, null=True, blank=True)
    image = models.ImageField(default=None, null=True, blank=True)
    total_gold = models.FloatField(default=0, null=True, blank=True)

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''