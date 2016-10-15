#-*- coding:utf-8 -*-
"""
Base views.
"""
from django.shortcuts import render
from django.views.decorators.http import require_GET

@require_GET
def home(request):
    """
    Homepage.
    """
    return render(request,'base/home.html')
