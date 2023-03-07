from django.urls import path
from .views import *

urlpatterns = [
      path('reg/', RegiView.as_view(),name='reg'),  
      path('log/',UserLogView.as_view(),name="log"),
      path('out/',SignOut.as_view(),name="out"),
      

]
