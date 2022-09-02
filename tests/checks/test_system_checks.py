# -*- coding: utf-8 -*-

# django-security-txt
# tests/checks/test_system_checks.py


from typing import List

from django.test import TestCase
from django.template import Context, Template
from django.test.utils import override_settings
from django.utils.translation import override as override_translation

from security_txt.models.hiring import Hiring
from security_txt.models.policy import Policy
from security_txt.models.contact import Contact
from security_txt.models.canonical import Canonical
from security_txt.views import get_security_txt_data
from security_txt.models.encryption import Encryption
from security_txt.models.acknowledgment import Acknowledgment


__all__: List[str] = ["SecurityTxtCheckTest"]


class SecurityTxtCheckTest(TestCase):
    """Test all the system checks."""
    pass
