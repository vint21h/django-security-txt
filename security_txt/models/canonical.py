# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/models/canonical.py


from typing import List

from django.db import models
from django.core.validators import URLValidator
from django.utils.translation import gettext_lazy as _


__all__: List[str] = ["Canonical"]


class Canonical(models.Model):  # noqa: DJ10,DJ1
    """Canonical model."""

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
        """Model settings."""

        app_label: str = "security_txt"
        verbose_name: str = _("canonical")
        verbose_name_plural: str = _("canonicals")
        ordering: List[str] = ["url"]

    def __str__(self) -> str:
        """
        Model representation.

        :return: canonical URL
        :rtype: str
        """
        return self.__unicode__()

    def __unicode__(self) -> str:
        """
        Model representation.

        :return: canonical URL
        :rtype: str
        """
        return self.url

    def __repr__(self) -> str:
        """
        Model representation.

        :return: canonical URL
        :rtype: str
        """
        return self.__unicode__()
