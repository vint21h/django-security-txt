# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/models/__init__.py


from typing import List  # pylint: disable=W0611

from security_txt.models.contact import Contact
from security_txt.models.canonical import Canonical
from security_txt.models.acknowledgment import Acknowledgment


__all__ = ["Acknowledgment", "Canonical", "Contact"]  # type: List[str]