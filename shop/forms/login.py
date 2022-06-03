from typing import Any
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(
        attrs={
            'class': 'form-control form-control-lg',
            'placeholder': "username"}),
    )
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control form-control-lg',
            'placeholder': "password"}),
    )
