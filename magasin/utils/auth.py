#-*- coding:utf-8 -*-
"""
Authentication backend that required to call the api
aka baguette-server.
"""
from django.conf import settings
from django.contrib.auth import get_user_model
from magasin.utils import Request

class APIAuthBackend(object):
    """
    Authentication class.
    Requires at least 2 methods:
        - authenticate()
        - get_user()
    """

    def authenticate(self, email=None, password=None, request=None):
        """
        Required method. Call the API to login using an email and password.
        """
        User = get_user_model()
        api = Request(settings.API_URL)
        response = api.post('accounts/login/',
                            {'email': email,
                             'password': password
                            })
        if response['status'] != 0:
            return None
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:#pylint:disable=no-member
            user = User(email=email)
            user.is_staff = False
            user.is_superuser = False
            user.save()
        finally:
            user.token = response['result']['token']#pylint:disable=unsubscriptable-object
        return user


    def get_user(self, user_id):
        """
        Required method.
        One authenticated, instanciate a dummy user object.
        """
        User = get_user_model()
        return User()
