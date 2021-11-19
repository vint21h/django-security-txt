# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/conf.py


from typing import List
from datetime import datetime  # noqa: F401

from appconf import AppConf
from django.conf import settings


__all__: List[str] = ["settings"]


class DjangoSecurityTxtAppConf(AppConf):
    """Django security.txt settings."""

    EXPIRES: datetime = getattr(settings, "SECURITY_TXT_EXPIRES", None)
    PREFERRED_LANGUAGES: List[str] = getattr(
        settings, "SECURITY_TXT_PREFERRED_LANGUAGES", None
    )
    SIGN: bool = getattr(settings, "SECURITY_TXT_SIGN", False)
    SIGN_KEY: str = getattr(settings, "SECURITY_TXT_SIGNING_KEY", "")

    class Meta:
        """Config settings."""

        prefix: str = "security_txt"
