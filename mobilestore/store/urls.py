from django.urls import path
from .views import *

urlpatterns = [
      path('store',StoreView.as_view(),name='store'), 
      path("addpro",AddProduct.as_view(),name="addpro"),
      path("viewpro",ViewPro.as_view(),name="viewpro") ,
      path('prodel/<int:id>',ProDelete.as_view(),name='prodel'),
      path('editpro/<int:id>',EditPro.as_view(),name='editpro')
      
      

]
