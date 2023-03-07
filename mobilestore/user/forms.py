from django import forms
from .models import Order
from account.models import User

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields="__all__"
