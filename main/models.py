
from email.mime import image
from email.policy import default
from users.models import UsersAb
from django.db import models

class Skins(models.Model):
    skin = models.CharField(max_length=255)
    image = models.ImageField(upload_to="SKINS/", default=None)

class Orders(models.Model):
    user = models.ForeignKey(UsersAb, models.CASCADE, null=False, blank=True)
    skin = models.CharField(max_length=255, null=True, blank=True)
    gold = models.FloatField(default=0)
    gold_commision = models.FloatField(default=0)
    data = models.DateTimeField(auto_now=True,null=True, blank=True)
    is_ordered = models.BooleanField(default=False, null=True, blank=True)

 
class CasesCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Cases(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="CASES/")
    price = models.FloatField(default=0)
    category = models.ForeignKey(CasesCategory, on_delete = models.CASCADE)

    def __str__(self):
        return self.name


    
