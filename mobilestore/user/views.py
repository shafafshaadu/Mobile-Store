from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import View,CreateView,FormView,TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import OrderForm
from .models import Order
from store.models import Add_Pro
from django.contrib.auth.models import User
from django.urls import reverse_lazy


# Create your views here.

class UserProView(View):
    def get(self,req):
        data=Add_Pro.objects.all()
        return render(req,"viewprouser.html",{"data":data}) 
class Products(View):
    def get(self,req):
        data=Add_Pro.objects.all()

        return render(req,"products.html",{"data":data}) 

# class OrderPro(View):
#     def get(self,req): 
#         return render(req,"order.html")

#     def post(self,req,*args,**kwargs):
#        form=OrderForm()
#        form_data=Order.objects.get()
#        return render(req,"order.html",{"forms":form})

class OrderPro(CreateView):
    model=Order
    form_class=OrderForm
    template_name='order.html'
    
    success_url=reverse_lazy('products')
    

class MyOrder(View):
    def get(self,req,*args,**kwargs):
        d_id=kwargs.get('id')
        dept=Order.objects.get(productname=d_id)
        form=OrderForm(instance=dept)
        return render(req,"myorder.html",{'form':form})
     
                   

