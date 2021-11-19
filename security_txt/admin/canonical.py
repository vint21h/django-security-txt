# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/admin/canonical.py


from typing import List

from django.contrib import admin


__all__: List[str] = ["CanonicalAdmin"]


class CanonicalAdmin(admin.ModelAdmin):  # type: ignore
    """Customize Canonical model for admin area."""

    list_display: List[str] = ["url"]
    search_fields: List[str] = ["url"]
