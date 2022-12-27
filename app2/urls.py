from django.urls import path
from app2.views import *
app_name='something2'
urlpatterns=[
    path('violet/',violet,name='violet'),
    path('indigo/',indigo,name='indigo'),
    path('blue/',blue,name='blue'),
]


