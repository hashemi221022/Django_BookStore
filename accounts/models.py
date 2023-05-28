from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True) # null for Database and blank for Form ### notice: for charfild toue dont should  null= True so you just blank= True and null= False
