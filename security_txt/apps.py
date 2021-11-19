# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/apps.py


from typing import List

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


__all__: List[str] = ["DjangoSecurityTxtConfig"]


class DjangoSecurityTxtConfig(AppConfig):
    """Django security.txt config."""

    name: str = "security_txt"
    verbose_name: str = _("Django security.txt")
