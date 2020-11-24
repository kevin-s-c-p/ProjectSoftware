from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request,"ProjectApp/login.html")


def index(request):

    return render(request,"ProjectApp/index.html")