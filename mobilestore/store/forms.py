from django import forms
from .models import Add_Pro
from account.models import User


class AddForm(forms.ModelForm):
    class Meta:
        model=Add_Pro
        fields="__all__"  

class storeForm(forms.ModelForm):
    class Meta:
        model=User
        fields="__all__"              