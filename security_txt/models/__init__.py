# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/models/__init__.py


from typing import List

from security_txt.models.hiring import Hiring
from security_txt.models.policy import Policy
from security_txt.models.contact import Contact
from security_txt.models.canonical import Canonical
from security_txt.models.encryption import Encryption
from security_txt.models.acknowledgment import Acknowledgment


__all__: List[str] = [
    "Acknowledgment",
    "Canonical",
    "Contact",
    "Hiring",
    "Policy",
    "Encryption",
]
