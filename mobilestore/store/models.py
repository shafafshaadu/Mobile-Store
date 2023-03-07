from django.db import models

# Create your models here.
class Add_Pro(models.Model):
    product_name=models.CharField(max_length=100)
    price=models.IntegerField(null=True)
    quantity=models.IntegerField(null=True)
    productmodel=models.CharField(max_length=100)
    color=models.CharField(max_length=100,null=True)
    description=models.TextField()
    pic=models.ImageField(upload_to="profilepic",null=True)
