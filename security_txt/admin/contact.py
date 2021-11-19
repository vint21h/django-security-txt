# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/admin/contact.py


from typing import List

from django.contrib import admin


__all__: List[str] = ["ContactAdmin"]


class ContactAdmin(admin.ModelAdmin):  # type: ignore
    """Customize Contact model for admin area."""

    list_display: List[str] = ["pk", "type", "email", "phone", "url"]
    search_fields: List[str] = ["email", "phone", "url"]
    list_filter: List[str] = ["type"]
