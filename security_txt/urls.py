# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/urls.py


from typing import List, Union

from django.urls import path
from django.urls.resolvers import URLPattern, URLResolver

from security_txt.views import SecurityTxtView


__all__ = ["urlpatterns"]


# security.txt urls
urlpatterns: List[Union[URLPattern, URLResolver]] = [
    path(
        "",
        SecurityTxtView.as_view(),
        name="security-txt",
    ),
]
