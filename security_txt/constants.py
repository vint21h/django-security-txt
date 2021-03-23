# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/constants.py


from typing import List, Tuple  # pylint: disable=W0611

from django.utils.translation import gettext_lazy as _


__all__ = [
    "CONTACT_TYPE_EMAIL",
    "CONTACT_TYPE_PHONE",
    "CONTACT_TYPE_URL",
    "CONTACT_TYPE_CHOICES",
]  # type: List[str]


CONTACT_TYPE_EMAIL = 1  # type: int
CONTACT_TYPE_PHONE = 2
CONTACT_TYPE_URL = 3  # type: int
CONTACT_TYPE_CHOICES = (
    (CONTACT_TYPE_EMAIL, _("E-mail")),
    (CONTACT_TYPE_PHONE, _("Phone")),
    (CONTACT_TYPE_URL, _("URL")),
)  # type: Tuple[Tuple[int, str], Tuple[int, str], Tuple[int, str]]
