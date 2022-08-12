from pydoc import synopsis
from typing import Any
from django import forms
from ..models.article import Article


class SettForm(forms.ModelForm):
    # title = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-input'}))
    # synopsis = forms.CharField(max_length=312, required=True,widget=forms.TextInput(attrs={'class': 'form-input'}))
    # img = forms.ImageField(required=True)
    # url = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-input'}))
    class Meta:
        model = Article
        fields = ['title','synopsis', 'url', 'img']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'synopsis': forms.TextInput(attrs={'class': 'form-input'}),
            'url': forms.TextInput(attrs={'class': 'form-input'}),
        }