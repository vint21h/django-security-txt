# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/admin/encryption.py


from typing import List  # pylint: disable=W0611

from django.contrib import admin


__all__ = ["EncryptionAdmin"]  # type: List[str]


class EncryptionAdmin(admin.ModelAdmin):  # type: ignore
    """
    Customize Encryption model for admin area.
    """

    list_display = ["pk", "type", "url", "dns", "fingerprint"]  # type: List[str]
    search_fields = ["url", "dns", "fingerprint"]  # type: List[str]
    list_filter = ["type"]  # type: List[str]
