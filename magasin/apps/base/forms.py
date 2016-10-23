#-*- coding:utf-8 -*-
"""
Base forms.
"""

from django import forms
from django.conf import settings
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from magasin.utils import Request

class SigninForm(forms.Form):
    """
    Login form.
    """
    email = forms.EmailField(label=_('Email'), max_length=100)
    password = forms.CharField(label=_('Password'), max_length=100, widget=forms.PasswordInput())

    def clean(self):
        """
        Validate the login.
        """
        cleaned_data = super(SigninForm, self).clean()
        user = authenticate(email=cleaned_data['email'],
                            password=cleaned_data['password'])
        if not user:
            raise forms.ValidationError(
                _('Unable to login with provided credentials.')
            )
        #Successfull login
        self.user = user#pylint:disable=attribute-defined-outside-init,unsubscriptable-object

class SignupForm(forms.Form):
    """
    Signup form.
    """
    email = forms.EmailField(label=_('Email'), max_length=100)
    username = forms.CharField(label=_('Username'), max_length=100)
    password = forms.CharField(label=_('Password'), max_length=100, widget=forms.PasswordInput())
    confirm_password = forms.CharField(label=_('Confirm Password'), max_length=100,
                                       widget=forms.PasswordInput())

    def clean(self):
        """
        Validate the signup.
        """
        cleaned_data = super(SignupForm, self).clean()
        api = Request(settings.API_URL)
        result = api.post('accounts/register/',
                          {'email': cleaned_data['email'],
                           'username': cleaned_data['username'],
                           'password': cleaned_data['password'],
                           'confirm_password': cleaned_data['confirm_password'],
                          })
        if result['status'] != 0:
            raise forms.ValidationError(
                result['error'].values()[0]
            )
