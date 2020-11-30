from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required

from ProjectApp.forms import registerUser

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
    
    form = registerUser()

    if request.method=='POST':
        form = registerUser(request.POST)
        if form.is_valid():
            form.save()

    

    return render(request,"ProjectApp/index.html",{'form':form})

def files(request):

    return render(request,"ProjectApp/files.html")

def add_file(request):

    return render(request,"ProjectApp/addfile.html")

def to_user(request):

    return render(request,"ProjectApp/users.html")