from django.urls import path
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from ProjectApp import views

urlpatterns = [
    path('accounts/login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout_user'),
    path('',login_required(views.index), name='index'),
]