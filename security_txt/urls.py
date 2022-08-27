# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/urls.py


from typing import List, Union

from django.urls import path
from django.views.generic import TemplateView
from django.urls.resolvers import URLPattern, URLResolver

from security_txt.conf import settings


__all__ = ["urlpatterns"]


# security.txt urls
urlpatterns: List[Union[URLPattern, URLResolver]] = [
    path(
        "",
        TemplateView.as_view(
            template_name="security_txt/security_txt.txt",
            extra_context={"SIGN": settings.SECURITY_TXT_SIGN},  # type: ignore
            # See: https://datatracker.ietf.org/doc/id/draft-foudil-securitytxt-10.txt
            # It MUST have a Content-Type of "text/plain" with the default charset
            # parameter set to "utf-8" (as per section 4.1.3 of [RFC2046]).
            content_type="text/plain",
        ),
        name="security-txt",
    ),
]
