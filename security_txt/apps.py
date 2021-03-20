# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/apps.py


from typing import List  # pylint: disable=W0611

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


__all__ = ["DjangoSecurityTxtConfig"]  # type: List[str]


class DjangoSecurityTxtConfig(AppConfig):
    """
    Django security.txt config.
    """

    name = "security_txt"  # type: str
    verbose_name = _("Django security.txt")  # type: str
