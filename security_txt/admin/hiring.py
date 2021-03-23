# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/admin/hiring.py


from typing import List  # pylint: disable=W0611

from django.contrib import admin


__all__ = ["HiringAdmin"]  # type: List[str]


class HiringAdmin(admin.ModelAdmin):  # type: ignore
    """
    Customize Hiring model for admin area.
    """

    list_display = ["url"]  # type: List[str]
    search_fields = ["url"]  # type: List[str]
