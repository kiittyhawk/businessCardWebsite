from typing import Any
from django import forms


class SettForm(forms.Form):
    title = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-input'}))
    synopsis = forms.CharField(max_length=312, required=True,widget=forms.TextInput(attrs={'class': 'form-input'}))
    img = forms.ImageField(required=True)
    url = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-input'}))