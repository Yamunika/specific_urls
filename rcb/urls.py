from django.urls import path
from rcb.views import *
urlpatterns=[
    path('captain/', captain,name='captain'),
     path('nextcaptain/', nextcaptain ,name='nextcaptain'),
   
]