# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/urls.py


from typing import List, Union  # pylint: disable=W0611

from django.conf.urls import url
from django.views.generic import TemplateView
from django.urls.resolvers import URLPattern, URLResolver  # pylint: disable=W0611

from security_txt.conf import settings


__all__ = ["urlpatterns"]


# security.txt urls
urlpatterns = [
    url(
        r"^$",
        TemplateView.as_view(
            template_name="security_txt/security_txt.txt",
            extra_context={"SIGN": settings.SECURITY_TXT_SIGN},  # type: ignore
        ),
        name="security-txt",
    ),
]  # type: List[Union[URLPattern, URLResolver]]
