# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/admin/policy.py


from typing import List

from django.contrib import admin


__all__: List[str] = ["PolicyAdmin"]


class PolicyAdmin(admin.ModelAdmin):  # type: ignore
    """Customize Policy model for admin area."""

    list_display: List[str] = ["url"]
    search_fields: List[str] = ["url"]
