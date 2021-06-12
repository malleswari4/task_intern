from App.models import *
from django import forms
from django.core import validators
from django.forms import ModelForm
from .models import User_Register

class LoginForm(forms.ModelForm):
    class Meta:
        model=User_Login
        fields='__all__'

class RegisterForm(forms.ModelForm):
    class Meta:
        model=User_Register
        fields='__all__'