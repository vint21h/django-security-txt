# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/admin/__init__.py


from typing import List  # pylint: disable=W0611

from django.contrib import admin

from security_txt.models.contact import Contact
from security_txt.admin.contact import ContactAdmin
from security_txt.models.canonical import Canonical
from security_txt.admin.canonical import CanonicalAdmin
from security_txt.models.acknowledgment import Acknowledgment
from security_txt.admin.acknowledgment import AcknowledgmentAdmin


__all__ = ["AcknowledgmentAdmin", "CanonicalAdmin", "ContactAdmin"]  # type: List[str]


# registering admin custom classes
admin.site.register(Acknowledgment, AcknowledgmentAdmin)
admin.site.register(Canonical, CanonicalAdmin)
admin.site.register(Contact, ContactAdmin)
