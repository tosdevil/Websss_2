from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

from django.forms import ModelForm, TextInput, PasswordInput


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Придумайте логин'
            }),
            "password1": forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Придумайте пароль'
            }),
            "password2": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Повторите пароль'
            }),
        }
