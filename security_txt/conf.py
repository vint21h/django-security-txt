# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/conf.py


from typing import List  # pylint: disable=W0611
from datetime import date  # noqa: F401  # pylint: disable=W0611

from appconf import AppConf
from django.conf import settings


__all__ = ["settings"]  # type: List[str]


class DjangoSecurityTxtAppConf(AppConf):
    """
    Django security.txt settings.
    """

    class Meta:
        """
        Config settings.
        """

        prefix = "security_txt"  # type: str
