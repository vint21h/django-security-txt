# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/admin/hiring.py


from typing import List

from django.contrib import admin


__all__: List[str] = ["HiringAdmin"]


class HiringAdmin(admin.ModelAdmin):  # type: ignore
    """Customize Hiring model for admin area."""

    list_display: List[str] = ["url"]
    search_fields: List[str] = ["url"]
