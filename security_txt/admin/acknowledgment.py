# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/admin/acknowledgment.py


from typing import List  # pylint: disable=W0611

from django.contrib import admin


__all__ = ["AcknowledgmentAdmin"]  # type: List[str]


class AcknowledgmentAdmin(admin.ModelAdmin):  # type: ignore
    """
    Customize Acknowledgment model for admin area.
    """

    list_display = ["url"]  # type: List[str]
    search_fields = ["url"]  # type: List[str]
