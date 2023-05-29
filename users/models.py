from email.policy import default
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import AbstractUser


class UsersAb(AbstractUser):
    USER = 'user'
    ADMIN = 'admin'
    YT = 'youtuber'
    ROLES = [
        (USER, 'user'),
        (ADMIN, 'admin'),
        (YT, 'youtuber'),
    ]
    role = models.CharField(max_length=255, choices=ROLES, default=USER, blank=True)
    gold = models.FloatField(default=0, null=True, blank=True)
    sum = models.FloatField(default=0, null=True, blank=True)
    image = models.ImageField(default=None, null=True, blank=True, upload_to='Users/', height_field=None, width_field=None, max_length=100)
    total_gold = models.FloatField(default=0, null=True, blank=True)
    open_box = models.IntegerField(default=0, null=True, blank=True)
    tg = models.CharField(max_length=255, null=True, blank=True)
    number = models.CharField(max_length=255, null=True, blank=True)
    is_ban = models.BooleanField(default=False)

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''