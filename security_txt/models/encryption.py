# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/models/encryption.py


from typing import List, Iterable, Optional  # pylint: disable=W0611

from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import URLValidator, RegexValidator

from security_txt.constants import (
    ENCRYPTION_TYPE_DNS,
    ENCRYPTION_TYPE_URL,
    ENCRYPTION_DNS_REGEX,
    ENCRYPTION_TYPE_CHOICES,
    ENCRYPTION_TYPE_FINGERPRINT,
    ENCRYPTION_FINGERPRINT_REGEX,
)


__all__ = ["Encryption"]  # type: List[str]


class Encryption(models.Model):
    """
    Encryption model.
    """

    TYPE_URL, TYPE_DNS, TYPE_FINGERPRINT = (
        ENCRYPTION_TYPE_URL,
        ENCRYPTION_TYPE_DNS,
        ENCRYPTION_TYPE_FINGERPRINT,
    )
    TYPE_CHOICES = ENCRYPTION_TYPE_CHOICES

    type = models.PositiveIntegerField(
        verbose_name=_("type"),
        help_text=_(
            f"contact type, possible variants: {', '.join(str(type) for type in dict(TYPE_CHOICES).values())}"  # noqa: E501
        ),
        db_index=True,
        choices=TYPE_CHOICES,
        default=TYPE_URL,
    )
    url = models.URLField(
        verbose_name=_("URL"),
        help_text=_("URL to public OpenPGP key"),
        max_length=512,
        db_index=True,
        blank=True,
        null=True,
        validators=[URLValidator(schemes=["https"])],
    )
    dns = models.CharField(
        verbose_name=_("DNS record"),
        help_text=_("OPENPGPKEY DNS record"),
        max_length=512,
        db_index=True,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=ENCRYPTION_DNS_REGEX,
                message=_(
                    "Invalid OPENPGPKEY DNS record, more information: https://tools.ietf.org/html/rfc7929"  # noqa: E501
                ),
            )
        ],
    )
    fingerprint = models.CharField(
        verbose_name=_("key fingerprint"),
        help_text=_("OpenPGP key fingerprint"),
        max_length=512,
        db_index=True,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=ENCRYPTION_FINGERPRINT_REGEX,
                message=_("Invalid OpenPGP key fingerprint"),
            )
        ],
    )

    class Meta:
        """
        Model settings.
        """

        app_label = "security_txt"  # type: str
        verbose_name = _("encryption")  # type: str
        verbose_name_plural = _("encryption")  # type: str
        ordering = ["type"]  # type: List[str]
        unique_together = [
            "type",
            "url",
            "dns",
            "fingerprint",
        ]  # type: List[str]

    def __unicode__(self) -> str:
        """
        Model representation.

        :return: corresponding type value
        :rtype: str
        """

        return {  # type: ignore
            self.TYPE_URL: self.url,
            self.TYPE_DNS: f"dns:{self.dns}",
            self.TYPE_FINGERPRINT: f"openpgp4fpr:{self.fingerprint}",
        }[self.type]

    def __str__(self) -> str:
        """
        Model representation.

        :return: corresponding type value
        :rtype: str
        """

        return self.__unicode__()

    def __repr__(self) -> str:
        """
        Model representation.

        :return: corresponding type value
        :rtype: str
        """

        return self.__unicode__()

    def save(
        self,
        force_insert: bool = False,
        force_update: bool = False,
        using: Optional[str] = None,
        update_fields: Optional[Iterable[str]] = None,
    ):
        """
        Overridden to call self.clean.

        :param force_insert: force insert data
        :type force_insert: bool
        :param force_update: force update data
        :type force_update: bool
        :param using: db name
        :type using: Optional[str]
        :param update_fields: list of fields to update
        :type update_fields: Optional[Iterable[str]]
        :return: self instance
        :rtype: Category
        """

        self.clean()

        return super(Encryption, self).save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )

    def clean(self) -> None:
        """
        Some checks.

        :raises ValidationError: in case of empty corresponding type field
        """

        if not {
            self.TYPE_URL: self.url,
            self.TYPE_DNS: self.dns,
            self.TYPE_FINGERPRINT: self.fingerprint,
        }[self.type]:
            raise ValidationError(
                message=_(
                    f"Provide corresponding type field value: {self.get_type_display()}"
                ),
                code="invalid",
            )
