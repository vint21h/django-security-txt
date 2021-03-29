# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/templatetags/security_txt_tags.py


from pathlib import Path
from typing import Any, Dict, List  # pylint: disable=W0611

from pgpy import PGPKey
from django import template
from django.core.exceptions import ImproperlyConfigured

from security_txt.conf import settings
from security_txt.models.hiring import Hiring
from security_txt.models.policy import Policy
from security_txt.models.contact import Contact
from security_txt.models.canonical import Canonical
from security_txt.models.encryption import Encryption
from security_txt.models.acknowledgment import Acknowledgment


__all__ = ["security_txt"]  # type: List[str]


register = template.Library()


@register.inclusion_tag("security_txt/templatetags/security_txt.txt")
def security_txt() -> Dict[str, Any]:
    """
    Render security.txt.

    :return: templatetag context data
    :rtype: Dict[str, Any]
    """

    return {
        "SECURITY_TXT_ACKNOWLEDGMENTS": Acknowledgment.objects.all(),
        "SECURITY_TXT_CANONICALS": Canonical.objects.all(),
        "SECURITY_TXT_CONTACTS": Contact.objects.all(),
        "SECURITY_TXT_ENCRYPTION": Encryption.objects.all(),
        "SECURITY_TXT_EXPIRES": settings.SECURITY_TXT_EXPIRES,
        "SECURITY_TXT_HIRING": Hiring.objects.all(),
        "SECURITY_TXT_POLICIES": Policy.objects.all(),
        "SECURITY_TXT_PREFERRED_LANGUAGES": settings.SECURITY_TXT_PREFERRED_LANGUAGES,
    }


@register.inclusion_tag("security_txt/templatetags/sign_security_txt.txt")
def sign_security_txt(data: str) -> Dict[str, str]:
    """
    Sign security.txt.

    :param data: data to sign
    :type data: str
    :return: templatetag context data
    :rtype: Dict[str, str]
    :raises ImproperlyConfigured: in case of bad signing config
    """

    if (settings.SECURITY_TXT_SIGN and not settings.SECURITY_TXT_SIGNING_KEY) or (  # type: ignore  # noqa: E501
        not Path(settings.SECURITY_TXT_SIGNING_KEY).exists()  # type: ignore  # noqa: E501
    ):

        raise ImproperlyConfigured

    key, _ = PGPKey.from_file(filename=settings.SECURITY_TXT_SIGNING_KEY)  # type: ignore  # noqa: E501

    return {
        "DATA": data,
        "SIGNATURE": key.sign(subject=data),
    }
