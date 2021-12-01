from django.db import models

# Create your models here.
class regi(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password1=models.CharField(max_length=12)

