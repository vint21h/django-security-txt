# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/admin/canonical.py


from typing import List  # pylint: disable=W0611

from django.contrib import admin


__all__ = ["CanonicalAdmin"]  # type: List[str]


class CanonicalAdmin(admin.ModelAdmin):  # type: ignore
    """
    Customize Canonical model for admin area.
    """

    list_display = ["url"]  # type: List[str]
    search_fields = ["url"]  # type: List[str]
