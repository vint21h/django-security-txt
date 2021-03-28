# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/templatetags/security_txt_tags.py


from datetime import datetime
from typing import Dict, List, Union  # pylint: disable=W0611

from django import template
from django.db.models import Manager

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
def security_txt() -> Dict[
    str,
    Union[
        Manager[Acknowledgment],
        Manager[Canonical],
        Manager[Contact],
        Manager[Encryption],
        datetime,
        Manager[Hiring],
        Manager[Policy],
        List[str],
    ],
]:
    """
    Render security.txt.

    :return: templatetag context data
    :rtype: Dict[str, Union[Manager[Acknowledgment], Manager[Canonical], Manager[Contact], Manager[Encryption], datetime, Manager[Hiring], Manager[Policy], List[str]]]
    """  # noqa: E501

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
