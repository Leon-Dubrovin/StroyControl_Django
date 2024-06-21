from django.contrib.auth.models import User
from django.db import models
from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage(location='/stroycontrol/static/images/')

class Predpisania(models.Model):
    Zakazchik = models.CharField(max_length=63)
    Podryadchik = models.CharField(max_length=63)
    Id = models.CharField(max_length=31)
    Narushenie = models.CharField(max_length=255)
    NTD = models.CharField(max_length=255)
    predp_date = models.DateField()
    exp_date = models.DateField()
    SK_FIO = models.CharField(max_length=63)

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()