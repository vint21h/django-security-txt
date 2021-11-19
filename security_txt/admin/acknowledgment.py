# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/admin/acknowledgment.py


from typing import List

from django.contrib import admin


__all__: List[str] = ["AcknowledgmentAdmin"]


class AcknowledgmentAdmin(admin.ModelAdmin):  # type: ignore
    """Customize Acknowledgment model for admin area."""

    list_display: List[str] = ["url"]
    search_fields: List[str] = ["url"]
