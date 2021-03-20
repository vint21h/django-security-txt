# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/__init__.py


from typing import List  # pylint: disable=W0611


__all__ = ["default_app_config"]  # type: List[str]


default_app_config = "security_txt.apps.DjangoSecurityTxtConfig"  # type: str
