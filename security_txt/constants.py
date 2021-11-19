# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/constants.py


from typing import List, Tuple

from django.utils.translation import gettext_lazy as _


__all__: List[str] = [
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
]


CONTACT_TYPE_EMAIL: int = 1
CONTACT_TYPE_PHONE: int = 2
CONTACT_TYPE_URL: int = 3
CONTACT_TYPE_CHOICES: Tuple[Tuple[int, str], ...] = (
    (CONTACT_TYPE_EMAIL, _("E-mail")),
    (CONTACT_TYPE_PHONE, _("Phone")),
    (CONTACT_TYPE_URL, _("URL")),
)

ENCRYPTION_TYPE_URL: int = 1
ENCRYPTION_TYPE_DNS: int = 2
ENCRYPTION_TYPE_FINGERPRINT: int = 3
ENCRYPTION_TYPE_CHOICES: Tuple[Tuple[int, str], ...] = (
    (ENCRYPTION_TYPE_URL, _("URL")),
    (ENCRYPTION_TYPE_DNS, _("OPENPGPKEY DNS record")),
    (ENCRYPTION_TYPE_FINGERPRINT, _("OpenPGP key fingerprint")),
)

ENCRYPTION_DNS_REGEX: str = r"([0-9 A-F a-f]{16,64})(._openpgpkey.)((?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9])(\?type=OPENPGPKEY$)"  # noqa: E501
ENCRYPTION_FINGERPRINT_REGEX: str = r"([0-9 A-F a-f]{16,64}$)"
