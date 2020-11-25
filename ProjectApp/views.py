from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def login_user(request):
    message = "Welcome"

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('login')
        
        else:
            message = "Username or Password incorrect"


    return render(request,"ProjectApp/login.html",{'message':message})


def index(request):

    return render(request,"ProjectApp/index.html")