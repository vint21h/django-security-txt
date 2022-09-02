# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/checks.py

from typing import Any, List

from django.core.checks import Error, Warning, register, Tags
from django.conf import settings
from django.apps import AppConfig


@register(Tags.files)
def check_if_key_exists_n_valid(apps_config: List[AppConfig], *__: Any, **___: Any) -> List[Error]:
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

def check_for_min_one_contact() -> List[Warning]:
    """
    Give a warning if not at least one contact is defined. 
    :return: list with one warning
    :rtype: List[]
    """
    pass

def check_for_expiration_date() -> List[Warning]:
    """
    Give a warning if expiration date is in the past.
    :return: list with one warning
    :rtype: List[Warning]
    """
    pass

def check_root_url() -> List[Warning]:
    """
    Give a warning if root_url doesn't accord to standard path as /.well-known/security.txt or /security.txt
    :return: list with one warning
    :rtype: List[]
    """
    pass