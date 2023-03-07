from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import View,CreateView,FormView
from .forms import UserRegform,LoginInForms
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.

class Home(View):
    def get(self,req):
        return render(req,'home.html')


class RegiView(CreateView):
    model=User
    form_class=UserRegform
    template_name='reg.html'
    success_url=reverse_lazy('home')
def post(self,request,*args,**kwargs):
    form_data=self.form_class(request.POST)
    if form_data.is_valid():
        messages.success(request,"Registration Completed!!!")
        return redirect('log')
    else:
        messages.error(request,"Registration failed")
        return render(request,"reg.html",{'form':form_data})

class UserLogView(FormView):
    template_name='log.html'
    form_class=LoginInForms
    success_url=reverse_lazy('home')
    def post(self,request):
      un=request.POST.get('username')
      pw=request.POST.get('password')
      user=authenticate(request,username=un,password=pw)
      if user:
        if user.usertype=="store":
            login(request,user)
            return redirect("store")
 
        elif user.usertype=="n_user":
            login(request,user)
            return redirect("usprvi")
      else:
        messages.error(request,"incorrect password") 
        return redirect("log") 
       

class SignOut(View):
    def get(self,req,*args,**kwargs):
        logout(req)
        return redirect('log')  



        
    
