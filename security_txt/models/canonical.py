# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/models/canonical.py


from typing import List  # pylint: disable=W0611

from django.db import models
from django.core.validators import URLValidator
from django.utils.translation import gettext_lazy as _


__all__ = ["Canonical"]  # type: List[str]


class Canonical(models.Model):
    """
    Canonical model.
    """

    url = models.URLField(
        verbose_name=_("URL"),
        help_text=_(
            "indicates the canonical URIs where the security.txt file is located"
        ),
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
        verbose_name = _("canonical")  # type: str
        verbose_name_plural = _("canonicals")  # type: str
        ordering = ["url"]  # type: List[str]

    def __unicode__(self) -> str:
        """
        Model representation.

        :return: canonical URL
        :rtype: str
        """

        return self.url

    def __str__(self) -> str:
        """
        Model representation.

        :return: canonical URL
        :rtype: str
        """

        return self.__unicode__()

    def __repr__(self) -> str:
        """
        Model representation.

        :return: canonical URL
        :rtype: str
        """

        return self.__unicode__()
