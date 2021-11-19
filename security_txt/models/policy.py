# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/models/policy.py


from typing import List

from django.db import models
from django.core.validators import URLValidator
from django.utils.translation import gettext_lazy as _


__all__: List[str] = ["Policy"]


class Policy(models.Model):  # noqa: DJ10,DJ1
    """Policy model."""

    url = models.URLField(
        verbose_name=_("URL"),
        help_text=_(
            "indicates a link to where the vulnerability disclosure policy is located"
        ),
        max_length=512,
        db_index=True,
        unique=True,
        validators=[URLValidator(schemes=["https"])],
    )

    class Meta:
        """Model settings."""

        app_label: str = "security_txt"
        verbose_name: str = _("policy")
        verbose_name_plural: str = _("policies")
        ordering: List[str] = ["url"]

    def __str__(self) -> str:
        """
        Model representation.

        :return: policy URL
        :rtype: str
        """
        return self.__unicode__()

    def __unicode__(self) -> str:
        """
        Model representation.

        :return: policy URL
        :rtype: str
        """
        return self.url

    def __repr__(self) -> str:
        """
        Model representation.

        :return: policy URL
        :rtype: str
        """
        return self.__unicode__()
