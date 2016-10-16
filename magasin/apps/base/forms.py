#-*- coding:utf-8 -*-
"""
Base forms.
"""
from django import forms

class SigninForm(forms.Form):
        email_username = forms.CharField(label='Username/Email', max_length=100)
        password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput())

