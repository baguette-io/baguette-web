#-*- coding:utf-8 -*-
"""
Base views.
"""
from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_GET
from .forms import SigninForm

@require_GET
def home(request):
    """
    Homepage.
    """
    return render(request,'base/home.html')

@require_http_methods(["GET", "POST"])
def signin(request):
    """
    Signin page.
    """
    form = SigninForm()
    return render(request, 'base/signin.html', {'form':form})

@require_http_methods(["GET", "POST"])
def signup(request):
    """
    Signup page.
    """
    return render(request, 'base/signup.html')
