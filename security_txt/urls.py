# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/urls.py


from typing import List, Union  # pylint: disable=W0611

from django.urls.resolvers import URLPattern, URLResolver  # pylint: disable=W0611


__all__ = ["urlpatterns"]


# security.txt urls
urlpatterns = []  # type: List[Union[URLPattern, URLResolver]]
