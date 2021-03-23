# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/models/hiring.py


from typing import List  # pylint: disable=W0611

from django.db import models
from django.core.validators import URLValidator
from django.utils.translation import gettext_lazy as _


__all__ = ["Hiring"]  # type: List[str]


class Hiring(models.Model):
    """
    Hiring model.
    """

    url = models.URLField(
        verbose_name=_("URL"),
        help_text=_("used for linking to the vendor's security-related job positions"),
        max_length=512,
        db_index=True,
        unique=True,
        validators=[URLValidator(schemes=["https"])],
    )

    class Meta:
        """
        Model settings.
        """

        app_label = "security_txt"  # type: str
        verbose_name = _("hiring")  # type: str
        verbose_name_plural = _("hiring")  # type: str
        ordering = ["url"]  # type: List[str]

    def __unicode__(self) -> str:
        """
        Model representation.

        :return: hiring URL
        :rtype: str
        """

        return self.url

    def __str__(self) -> str:
        """
        Model representation.

        :return: hiring URL
        :rtype: str
        """

        return self.__unicode__()

    def __repr__(self) -> str:
        """
        Model representation.

        :return: hiring URL
        :rtype: str
        """

        return self.__unicode__()
