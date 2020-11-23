from django.urls import path

from ProjectApp import views

urlpatterns = [
    path('',views.home, name='home'),
]