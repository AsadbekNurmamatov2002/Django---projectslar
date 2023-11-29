from django.urls import path
from .views import Home, Dars

urlpatterns=[
    path('',Home, name='home'),
    path('dars/<int:id>',Dars, name='dars'),

]