from django.urls import path
from .views import *

urlpatterns = [
      path('usprvi',UserProView.as_view(),name='usprvi'),
      path('products',Products.as_view(),name='products'),
      path('order',OrderPro.as_view(),name='order'),  
      path('myod',MyOrder.as_view(),name='myod'),  
     
      
      

]