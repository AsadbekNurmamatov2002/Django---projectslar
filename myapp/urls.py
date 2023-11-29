from django.urls import path
from .views import Darslik

urlpatterns=[
    path('darslik/',Darslik, name='darslik' ),
]