# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/models/languages.py


from typing import List
from dataclasses import dataclass
from faulthandler import is_enabled

from django.conf import settings


__all__: List[str] = ["Language"]


@dataclass
class Language:
    """Placeholder for Languages model."""

    prefix: str = "Preferred-Languages:"
    comment: str = ""
    _separator: str = ", "

    @property
    def is_enabled(self) -> bool:
        """ """
        return bool(settings.SECURITY_TXT_PREFERRED_LANGUAGES)

    def __str__(self) -> str:
        """
        Generates preferred languages, comma separated.

        :return: preferred languages
        :rtype: str
        """
        return self._separator.join(
            language for language in settings.SECURITY_TXT_PREFERRED_LANGUAGES
        )
