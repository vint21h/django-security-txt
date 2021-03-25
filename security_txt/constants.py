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
    "ENCRYPTION_TYPE_URL",
    "ENCRYPTION_TYPE_DNS",
    "ENCRYPTION_TYPE_FINGERPRINT",
    "ENCRYPTION_TYPE_CHOICES",
    "ENCRYPTION_DNS_REGEX",
    "ENCRYPTION_FINGERPRINT_REGEX",
]  # type: List[str]


CONTACT_TYPE_EMAIL = 1  # type: int
CONTACT_TYPE_PHONE = 2
CONTACT_TYPE_URL = 3  # type: int
CONTACT_TYPE_CHOICES = (
    (CONTACT_TYPE_EMAIL, _("E-mail")),
    (CONTACT_TYPE_PHONE, _("Phone")),
    (CONTACT_TYPE_URL, _("URL")),
)  # type: Tuple[Tuple[int, str], Tuple[int, str], Tuple[int, str]]

ENCRYPTION_TYPE_URL = 1
ENCRYPTION_TYPE_DNS = 2
ENCRYPTION_TYPE_FINGERPRINT = 3
ENCRYPTION_TYPE_CHOICES = (
    (ENCRYPTION_TYPE_URL, _("URL")),
    (ENCRYPTION_TYPE_DNS, _("OPENPGPKEY DNS record")),
    (ENCRYPTION_TYPE_FINGERPRINT, _("OpenPGP key fingerprint")),
)

ENCRYPTION_DNS_REGEX = r"([0-9 A-F a-f]{16,64})(._openpgpkey.)((?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9])(\?type=OPENPGPKEY$)"  # type: str  # noqa: E501
ENCRYPTION_FINGERPRINT_REGEX = r"([0-9 A-F a-f]{16,64}$)"  # type: str
