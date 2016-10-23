#-*- coding:utf-8 -*-
"""
Account views.
"""
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET


@login_required
@require_GET
def home(request):
    """
    Account Homepage.
    """
    return render(request, 'account/home.html', {'API_URL':settings.API_URL})
