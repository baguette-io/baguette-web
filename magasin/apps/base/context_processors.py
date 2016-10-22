#-*- coding:utf-8 -*-
"""
Add basic context processors.
"""

def is_connected(request):
    """
    Check if the user is connected
    by checking if he has a token cookie.
    """
    return {'is_connected': request.COOKIES.get('token', False)}
