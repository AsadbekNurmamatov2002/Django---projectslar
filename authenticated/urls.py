from django.urls import path
from .views import user_login, Registr, logout_user

urlpatterns=[
    path('login/',user_login, name='user_login'),
    path('registr/',Registr, name='registr'),
    path('logout/',logout_user, name='logout'),

]
