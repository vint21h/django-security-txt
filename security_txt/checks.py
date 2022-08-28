# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/checks.py

from typing import Any, List

from django.core.checks import Error, register, Tags
from django.conf import settings


@register(Tags.files)
def check_if_key_exists_n_valid(_: Any, *__: Any, **___: Any) -> List[Error]:
    """
    Check if key file exists and can be loaded if SECURITY_TXT_SIGN is set to True.

    :param apps_config: app configurations
    :type apps_config: AppConfig???
    :return: list of errors
    :rtype: List[Error]
    """
    errors: List[Error] = []
    SECURITY_TXT_SIGN: bool = settings.SECURITY_TXT_SIGN
    SECURITY_TXT_SIGNING_KEY: str = settings.SECURITY_TXT_SIGNING_KEY

    if SECURITY_TXT_SIGN:
        try:
            PGPKey.from_file(filename=SECURITY_TXT_SIGNING_KEY)  # type: ignore  # noqa: E501
        except (ValueError, PermissionError, FileNotFoundError):
            errors.append(
                Error(
                    "SECURITY_TXT_SIGN is set to True but no valid signing key can be found at SECURITY_TXT_SIGNING_KEY.",
                    hint="Check your SECURITY_TXT_SIGNING_KEY setting.",
                    obj=SECURITY_TXT_SIGNING_KEY,
                    id="security-txt.E001"
                )
            )
    
    return errors
