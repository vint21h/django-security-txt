# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/views.py


import datetime
from typing import List

from pgpy import PGPKey
from django.apps import apps
from django.views import View
from django.conf import settings
from django.http import HttpResponse
from django.core.exceptions import ImproperlyConfigured

from security_txt.models.languages import Language
from security_txt.constants import (
    CHARSET,
    PGP_HASH,
    SEPARATOR,
    CONTENT_TYPE,
    BEGIN_PGP_SIGNED_MESSAGE,
)


def get_security_txt_lines_by_model(model_class_name: str) -> List[str]:
    """
    Generates a list of strings for all relevant db entries.

    :param model_class_name: name of the model class
    :type model_class_name: str
    :return: list of security_txt strings
    :rtype: List[str]
    """
    security_txt_lines: List[str] = []
    model_class = apps.get_model("security_txt", model_class_name)
    model_qs = model_class.objects.all()
    if model_qs.exists():
        if model_class.comment:
            security_txt_lines.append(model_class.comment)
        for entry in model_qs:
            security_txt_lines.append(f"{model_class.prefix} {str(entry)}")
    return security_txt_lines


def get_security_txt_data() -> str:
    """
    Returns a string with all available entries.
    :return: security-txt string
    :rtype: str
    """
    security_txt_lines: List[str] = []
    security_txt_lines.extend(get_security_txt_lines_by_model("Acknowledgment"))
    security_txt_lines.extend(get_security_txt_lines_by_model("Canonical"))
    security_txt_lines.extend(get_security_txt_lines_by_model("Contact"))
    security_txt_lines.extend(get_security_txt_lines_by_model("Encryption"))

    SECURITY_TXT_EXPIRES: datetime = settings.SECURITY_TXT_EXPIRES
    if SECURITY_TXT_EXPIRES:
        # iso8601, see https://datatracker.ietf.org/doc/html/draft-foudil-securitytxt-12#section-3.5.5
        expires_date: str = SECURITY_TXT_EXPIRES.isoformat()
    else:
        expires_date: str = ""
    # MUST always be present
    security_txt_lines.append(f"Expires: {expires_date}")

    security_txt_lines.extend(get_security_txt_lines_by_model("Hiring"))
    security_txt_lines.extend(get_security_txt_lines_by_model("Policy"))

    # Languages are a little special here.
    languages = Language()
    if languages.is_enabled:
        if languages.comment:
            security_txt_lines.append(languages.comment)
        security_txt_lines.append(f"{languages.prefix} {languages}")

    return SEPARATOR.join(security_txt_lines)


def signed_security_txt_data(data: str) -> str:
    """
    Signs the security-txt content.

    :param data: security-txt string
    :return: signed security-txt content
    :rtype: str
    """
    signed_data: List[str] = []
    try:
        key, _ = PGPKey.from_file(filename=settings.SECURITY_TXT_SIGNING_KEY)  # type: ignore  # noqa: E501
    except (ValueError, PermissionError, FileNotFoundError):
        raise ImproperlyConfigured
    signature: str = str(key.sign(subject=data))
    signed_data.append(BEGIN_PGP_SIGNED_MESSAGE)
    signed_data.append(PGP_HASH)
    signed_data.append(data)
    signed_data.append(signature)
    return SEPARATOR.join(signed_data)


class SecurityTxtView(View):
    """Main view for security-txt app."""

    http_method_names: List[str] = ["get"]

    def get(self, *_, **__) -> HttpResponse:
        """The only method allowed.

        :param _: unused
        :type _: List[Any]
        :param __: unused
        :type __: Dict[Any, Any]
        :return: text/plain httpresponse with security.txt as content
        :rtype: HttpResponse
        """
        signed: bool = getattr(settings, "SECURITY_TXT_SIGN", False)  # type: ignore # noqa: E261

        security_txt_data: List[str] = get_security_txt_data()

        if signed:
            security_txt_data = signed_security_txt_data(security_txt_data)

        return HttpResponse(
            security_txt_data, content_type=CONTENT_TYPE, charset=CHARSET
        )
