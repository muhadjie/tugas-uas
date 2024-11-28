# userauths/forms.py
from django import forms  # type: ignore
from django.contrib.auth.forms import UserCreationForm  # type: ignore
from django.contrib.auth.models import User  # type: ignore  # Pastikan ini mengarah ke model User bawaan Django

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
