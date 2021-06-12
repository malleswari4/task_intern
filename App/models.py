from django.db import models
from django import forms

# Create your models here.
class User_Login(models.Model):
    user_email=models.CharField(max_length=100)
    user_password=models.CharField(max_length=30)


    def  __str__(self):
        return self.user_email

class User_Register(models.Model):
    reg_name=models.CharField(max_length=50)
    reg_email=models.CharField(max_length=70)
    reg_address=models.CharField(max_length=100)
    reg_pass=models.CharField(max_length=50)

    def  __str__(self):
        return self.reg_email+""+self.reg_name