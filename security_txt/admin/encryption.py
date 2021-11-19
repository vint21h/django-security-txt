# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/admin/encryption.py


from typing import List

from django.contrib import admin


__all__: List[str] = ["EncryptionAdmin"]


class EncryptionAdmin(admin.ModelAdmin):  # type: ignore
    """Customize Encryption model for admin area."""

    list_display: List[str] = ["pk", "type", "url", "dns", "fingerprint"]
    search_fields: List[str] = ["url", "dns", "fingerprint"]
    list_filter: List[str] = ["type"]
