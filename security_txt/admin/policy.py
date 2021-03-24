# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/admin/policy.py


from typing import List  # pylint: disable=W0611

from django.contrib import admin


__all__ = ["PolicyAdmin"]  # type: List[str]


class PolicyAdmin(admin.ModelAdmin):  # type: ignore
    """
    Customize Policy model for admin area.
    """

    list_display = ["url"]  # type: List[str]
    search_fields = ["url"]  # type: List[str]
