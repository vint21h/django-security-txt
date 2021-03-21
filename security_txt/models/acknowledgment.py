# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/models/acknowledgment.py


from typing import List  # pylint: disable=W0611

from django.db import models
from django.core.validators import URLValidator
from django.utils.translation import gettext_lazy as _


__all__ = ["Acknowledgment"]  # type: List[str]


class Acknowledgment(models.Model):
    """
    Acknowledgment model.
    """

    url = models.URLField(
        verbose_name=_("link to page where security researchers are recognized"),
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
        verbose_name = _("acknowledgment")  # type: str
        verbose_name_plural = _("acknowledgments")  # type: str
        ordering = ["url"]  # type: List[str]

    def __unicode__(self) -> str:
        """
        Model representation.

        :return: acknowledgment URL
        :rtype: str
        """

        return self.url

    def __str__(self) -> str:
        """
        Model representation.

        :return: thank to name
        :rtype: str
        """

        return self.__unicode__()

    def __repr__(self) -> str:
        """
        Model representation.

        :return: thank to name
        :rtype: str
        """

        return self.__unicode__()
