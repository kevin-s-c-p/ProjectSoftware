from django.urls import path
from django.contrib.auth import login, logout

from ProjectApp import views

urlpatterns = [
    path('',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout_user'),
    path('index/',views.index, name='index'),
]