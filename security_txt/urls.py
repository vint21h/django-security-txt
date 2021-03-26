# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/urls.py


from typing import List, Union  # pylint: disable=W0611

from django.conf.urls import url
from django.urls.resolvers import URLPattern, URLResolver  # pylint: disable=W0611

from security_txt.views import security_txt


__all__ = ["urlpatterns"]


# security.txt urls
urlpatterns = [
    url(r"^$", security_txt, name="security-txt")
]  # type: List[Union[URLPattern, URLResolver]]
