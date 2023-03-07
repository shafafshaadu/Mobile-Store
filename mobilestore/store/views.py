from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import View,CreateView,FormView,TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import storeForm,AddForm
from .models import Add_Pro
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.

class StoreView(TemplateView):
    template_name="store.html"
    model=User
    form_class=storeForm
    success_url=reverse_lazy('home')

class AddProduct(View):
    def get(self,req):
        model=Add_Pro()
        form_class=AddForm()
        return render(req,'addproduct.html',{'form':form_class})        

    def post(self,req,*args,**kwargs):
        form_data=AddForm(data=req.POST,files=req.FILES)
        
        if form_data.is_valid():
            form_data.save()
    
            messages.success(req,"product added!!!")
            return redirect('viewpro')

        else:
            print(form_data.errors)
            messages.error(req,"failed")
            return render(req,"addproduct.html")      

class ViewPro(View):
    def get(self,req):
        data=Add_Pro.objects.all()
        return render(req,"viewpro.html",{"data":data}) 
    
class ProDelete(View):
    def get(self,req,*args,**kwargs):
        did=kwargs.get('id')
        dell=Add_Pro.objects.get(id=did)
        dell.delete()
        return redirect('prodel')  

class EditPro(View):
    def get(self,req,*args,**kwargs):
        d_id=kwargs.get('id')
        dept=Add_Pro.objects.get(id=d_id)
        form=AddForm(instance=dept)
        return redirect(req,"editpro.html",{'form':form})       

def post(self,req,*args,**kwargs):
    d_id=kwargs.get('id')
    dept=Add_Pro.objects.get(id=d_id)
    form_data=AddForm(req.POST,instance=dept)
    if form_data.is_valid():
        form_data.save()
        return redirect('viewpro')
    else:
        messages.error(req,"failed")
        return redirect('editpro')       
