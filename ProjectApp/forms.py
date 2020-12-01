from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class loginform(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    # class Meta:
    #     fields = ['username']

class registerUser(UserCreationForm):
    
    class Meta:
        model = User
        fields = [
            'username',
            'is_staff',
            'first_name',
            'email'
        ]

        labels = {
            'username':'Nombre de usuario'
        }

