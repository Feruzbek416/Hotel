from django.urls import path
from .views import *

urlpatterns =[
    path('',Hotel,name='hotel')
]