from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required

from ProjectApp.forms import loginform, UserRegister

# Create your views here.



def login_user(request):
    template_name = "ProjectApp/login.html"
    message = "Welcome"

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None:
            if user.is_active:
                login(request, user)
                if request.GET.get('next',None):
                    return HttpResponseRedirect(request.GET['next'])
                else:
                    redirect('login')
        else:
            message = "Username or Password incorrect"


    return render(request,"ProjectApp/login.html",{'message':message,'template_name':template_name})


def logout_user(request):
    logout(request)
    return redirect('index')


def index(request):
    

    return render(request,"ProjectApp/index.html")