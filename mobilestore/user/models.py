from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    First_Name=models.CharField(max_length=100)
    Second_Name=models.CharField(max_length=100)
    Address=models.TextField()
    E_mail=models.EmailField()
    Phone=models.IntegerField()
    options=(
        ('COD','COD'),
        ('Debit/Credit_Card','Debit/Credit_Card'),
        ('UPI','UPI'))
    payment=models.CharField(max_length=100,choices=options,default='COD')


