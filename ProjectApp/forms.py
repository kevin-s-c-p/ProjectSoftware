from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class loginform(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    # class Meta:
    #     fields = ['username']

class UserRegister(forms.Form):
    username = forms.CharField(max_length=255)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    mail = forms.EmailField(widget=forms.EmailInput)
    options = (
        ( True, "Administrador"),
        ( False, "Empleado")
    )
    type_user = forms.ChoiceField(choices=options)

    class Meta:
        fields = [
            'username',
            'email',
            'password',
            'is_staff'
        ]
    
    def save(self):
        user = User.objects.create_user(self.username,self.mail,self.password1)

        user.is_staff = self.type_user
        user.superuser = self.type_user

        user.save()