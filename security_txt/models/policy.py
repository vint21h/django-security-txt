# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/models/policy.py


from typing import List  # pylint: disable=W0611

from django.db import models
from django.core.validators import URLValidator
from django.utils.translation import gettext_lazy as _


__all__ = ["Policy"]  # type: List[str]


class Policy(models.Model):
    """
    Policy model.
    """

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
        """
        Model settings.
        """

        app_label = "security_txt"  # type: str
        verbose_name = _("policy")  # type: str
        verbose_name_plural = _("policies")  # type: str
        ordering = ["url"]  # type: List[str]

    def __unicode__(self) -> str:
        """
        Model representation.

        :return: policy URL
        :rtype: str
        """

        return self.url

    def __str__(self) -> str:
        """
        Model representation.

        :return: policy URL
        :rtype: str
        """

        return self.__unicode__()

    def __repr__(self) -> str:
        """
        Model representation.

        :return: policy URL
        :rtype: str
        """

        return self.__unicode__()
