#-*- coding:utf-8 -*-
"""
Base views.
"""
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.http import require_http_methods, require_GET
from .forms import SigninForm, SignupForm

@require_GET
def home(request):
    """
    Homepage.
    """
    return render(request, 'base/home.html')

@require_http_methods(["GET", "POST"])
def signin(request):
    """
    Signin page.
    """
    if request.method == 'GET':
        form = SigninForm()
    else:
        form = SigninForm(request.POST)
        if form.is_valid():
            #Add the cookie to the client
            login(request, form.user)
            response = redirect('account.home')
            response.set_cookie('token', form.user.token)
            return response
    return render(request, 'base/signin.html', {'form':form})

@require_http_methods(["GET", "POST"])
def signup(request):
    """
    Signup page.
    """
    if request.method == 'GET':
        form = SignupForm()
    else:
        form = SignupForm(request.POST)
        if form.is_valid():
            #Success message and redirect to the login page
            messages.success(request, _('Account created. Please signin.'))
            response = redirect('signin')
            return response
    return render(request, 'base/signup.html', {'form':form})
