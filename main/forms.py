from enum import unique
from django import forms
from phonenumber_field.modelfields import PhoneNumberField

class CallMeForm(forms.Form):
    name = forms.CharField(max_length=128, label='Как к Вам обращаться?', widget=forms.TextInput(
        attrs={
            'class': 'form-control'}),
        )
    number = forms.CharField(min_length=11, label='Ваш номер телефона', widget=forms.TextInput(
        attrs={
            'class': 'form-control'}),
        )
    comment = forms.CharField(label='Комментарий(необязательно)', required=False, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'cols': 60,
            'rows': 5}),
        )