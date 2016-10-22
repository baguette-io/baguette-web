#-*- coding:utf-8 -*-
"""
Authentication backend that required to call the api
aka baguette-server.
"""
from django.contrib.auth.models import User


class AuthBackend(object):
    """
    Authentication class.
    Requires at least 2 methods:
        - authenticate()
        - get_user()
    """

    def authenticate(self, username=None, password=None, token=None):
        """
        Required method. Call the API.
        If login, set username and password will be set.
        If already login, token will be the one containing the session infos.
        """


    def get_user(self, user_id):
        """
        Required method.
        One authenticated, instanciate a dummy user object.
        """
        return User(pk=user_id)
