from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
import os

from ProjectApp.forms import registerUser, addfiles

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
                    if user.is_staff:
                        return HttpResponseRedirect(request.GET['next'])
                    else:
                        return redirect('addfiles')
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
    messege = "Welcome"

    if request.method=='POST':
        if request.user.is_staff:
            form = registerUser(request.POST)
            if form.is_valid():
                form.save()
                form = registerUser()
                redirect('index')
        else:
            messege = "No tienes Permisos de administrador"

    

    return render(request,"ProjectApp/index.html",{'form':form,'messege':messege})

def files(request):

    return render(request,"ProjectApp/files.html")

def add_file(request):
    message = "Ingrese su Archivo"
    form = addfiles()

    context = {
        'message':message,
        'form':form
    }

    if request.method == 'POST':
        form = addfiles(request.POST,request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.usuario = request.user
            arch = (str(form.archivo))#guardamos el archivo en tipo string
            form.extencion = exten(arch)
            form.tamaño = '10 kb'
            form.save()
        else:
            message = "Error en el Envio de formulario"

    return render(request,"ProjectApp/addfile.html",context)

def to_user(request):

    return render(request,"ProjectApp/users.html")

def exten(arch):
    arch2 = arch.split('.')

    return arch2[-1]