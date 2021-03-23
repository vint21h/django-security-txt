# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/admin/contact.py


from typing import List  # pylint: disable=W0611

from django.contrib import admin


__all__ = ["ContactAdmin"]  # type: List[str]


class ContactAdmin(admin.ModelAdmin):  # type: ignore
    """
    Customize Contact model for admin area.
    """

    list_display = ["pk", "type", "email", "phone", "url"]  # type: List[str]
    search_fields = ["email", "phone", "url"]  # type: List[str]
    list_filter = ["type"]  # type: List[str]
