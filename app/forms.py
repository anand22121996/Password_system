from django.forms import ModelForm
from .models import Login
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(ModelForm):
     class Meta:
         model = Login
         fields = ['profile', 'username', 'password']
         widgets = {
         	'profile': forms.TextInput(attrs={'class':'form-control rounded-pill', 'placeholder':'Enter Profile Name'}),
         	'username': forms.TextInput(attrs={'class':'form-control rounded-pill', 'placeholder':'Enter Username Name'}),
         	'password': forms.PasswordInput(attrs={'class':'form-control rounded-pill', 'placeholder':'Enter Password'})
         }



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']