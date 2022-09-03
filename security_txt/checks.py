# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/checks.py

from datetime import datetime
from typing import Any, List

from django.conf import settings
from django.apps import AppConfig
from django.core.checks import Tags, Error, Warning, register

from pgpy import PGPKey

from security_txt.models.contact import Contact
from tests.settings import ROOT_URLCONF

KEY_NOT_VALID_ERROR: Error = Error(
    "SECURITY_TXT_SIGN is set to True but no valid signing key can be found at SECURITY_TXT_SIGNING_KEY.",
    hint="Check your SECURITY_TXT_SIGNING_KEY setting.",
    id="security-txt.E001"
)
NO_CONTACT_WARNING: Warning = Warning(
    "Define at least one Contact for security-txt file.",
    obj=Contact,
    id="security-txt.W001",
)
EXPIRY_DATE_WARNING: Warning = Warning(
    "SECURITY_TXT_EXPIRES date is in the past.",
    id="security-txt.W002",
)
ROOT_URL_WARNING: Warning = Warning(
    "ROOT_URL of security-txt app is not standard.",
    id="security-txt.W002",
)

@register(Tags.files)
def check_if_key_exists_n_valid(_: List[AppConfig] = None, **__: Any) -> List[Error]:
    """
    Check if key file exists and can be loaded if SECURITY_TXT_SIGN is set to True.

    :param apps_config: app configurations
    :type apps_config: AppConfig???
    :return: list of errors
    :rtype: List[Error]
    """
    errors: List[Error] = []
    SECURITY_TXT_SIGN: bool = getattr(settings, 'SECURITY_TXT_SIGN', False)
    SECURITY_TXT_SIGNING_KEY: str = getattr(settings, 'SECURITY_TXT_SIGNING_KEY', False)
    if SECURITY_TXT_SIGN:
        try:
            PGPKey.from_file(filename=SECURITY_TXT_SIGNING_KEY)  # type: ignore  # noqa: E501
        except (ValueError, PermissionError, FileNotFoundError):
            errors.append(KEY_NOT_VALID_ERROR)
    return errors


@register(Tags.models)
def check_for_min_one_contact(_: List[AppConfig] = None, **__: Any) -> List[Warning]:
    """
    Give a warning if not at least one contact is defined.
    :return: list with one warning
    :rtype: List[]
    """
    warnings: List[Warning] = []
    if not Contact.objects.exists():
        warnings.append(NO_CONTACT_WARNING)
    return warnings


def check_for_expiration_date(_: List[AppConfig] = None, **__: Any) -> List[Warning]:
    """
    Give a warning if expiration date is in the past.
    :return: list with one warning
    :rtype: List[Warning]
    """
    warnings: List[Warning] = []
    SECURITY_TXT_EXPIRES: datetime = getattr(settings, 'SECURITY_TXT_EXPIRES')
    if SECURITY_TXT_EXPIRES < datetime.now():
        warnings.append(EXPIRY_DATE_WARNING)
    return warnings



def check_root_url(_: List[AppConfig] = None, **__: Any) -> List[Warning]:
    """
    Give a warning if root_url doesn't accord to standard path as /.well-known/security.txt or /security.txt
    :return: list with one warning
    :rtype: List[Warning]
    """
    warnings: List[Warning] = []
    warnings.append(ROOT_URL_WARNING)
    return warnings
