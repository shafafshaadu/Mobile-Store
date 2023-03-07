from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class UserRegform(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'first_name','last_name','email','password1','password2','phone','address','username','usertype'
        ]

class LoginInForms(forms.Form):
  username=forms.CharField(max_length=100)
  password=forms.CharField(max_length=100,widget=forms.PasswordInput())     
