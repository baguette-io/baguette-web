"""
magasin urls.
"""
from django.conf.urls import include, url

urlpatterns = [#pylint: disable=invalid-name
    url(r'^account/', include('magasin.apps.account.urls')),
    url(r'^', include('magasin.apps.base.urls')),
]
