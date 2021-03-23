# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/models/contact.py


from typing import List, Iterable, Optional  # pylint: disable=W0611

from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from security_txt.constants import (
    CONTACT_TYPE_URL,
    CONTACT_TYPE_EMAIL,
    CONTACT_TYPE_PHONE,
    CONTACT_TYPE_CHOICES,
)


__all__ = ["Contact"]  # type: List[str]


class Contact(models.Model):
    """
    Contact model.
    """

    TYPE_EMAIL, TYPE_PHONE, TYPE_URL = (
        CONTACT_TYPE_EMAIL,
        CONTACT_TYPE_PHONE,
        CONTACT_TYPE_URL,
    )
    TYPE_CHOICES = CONTACT_TYPE_CHOICES

    type = models.PositiveIntegerField(
        verbose_name=_("type"),
        help_text=_(
            f"contact type, possible variants: {', '.join(str(type) for type in dict(TYPE_CHOICES).values())}"  # noqa: E501
        ),
        db_index=True,
        choices=TYPE_CHOICES,
        default=TYPE_EMAIL,
    )
    email = models.EmailField(
        verbose_name=_("e-mail"),
        help_text=_("contact e-mail"),
        max_length=512,
        db_index=True,
        blank=True,
        null=True,
    )
    phone = PhoneNumberField(
        verbose_name=_("phone"),
        help_text=_("contact phone number"),
        db_index=True,
        blank=True,
        null=True,
    )
    url = models.URLField(
        verbose_name=_("URL"),
        help_text=_("contact page URL"),
        max_length=512,
        db_index=True,
        blank=True,
        null=True,
        validators=[URLValidator(schemes=["https"])],
    )

    class Meta:
        """
        Model settings.
        """

        app_label = "security_txt"  # type: str
        verbose_name = _("contact")  # type: str
        verbose_name_plural = _("contacts")  # type: str
        ordering = ["type"]  # type: List[str]
        unique_together = [
            "type",
            "email",
            "phone",
            "url",
        ]  # type: List[str]

    def __unicode__(self) -> str:
        """
        Model representation.

        :return: corresponding type value
        :rtype: str
        """

        return {  # type: ignore
            self.TYPE_EMAIL: f"mailto:{self.email}",
            self.TYPE_PHONE: f"tel:{self.phone}",
            self.TYPE_URL: self.url,
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

        return super(Contact, self).save(
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
            self.TYPE_EMAIL: self.email,
            self.TYPE_PHONE: self.phone,
            self.TYPE_URL: self.url,
        }[self.type]:
            raise ValidationError(message=_("Provide corresponding type field value"))
