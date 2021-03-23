# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/views.py


from datetime import datetime  # noqa: F401  # pylint: disable=W0611
from typing import Dict, List, Union  # noqa: F401  # pylint: disable=W0611

from django.shortcuts import render
from django.db.models import Manager
from django.http import HttpResponse
from django.http.request import HttpRequest

from security_txt.conf import settings
from security_txt.models.contact import Contact
from security_txt.models.canonical import Canonical
from security_txt.models.acknowledgment import Acknowledgment


__all__ = ["security_txt"]  # type: List[str]


def security_txt(request: HttpRequest) -> HttpResponse:
    """
    Return security.txt.

    :param request: django request instance
    :type request: HttpRequest
    :return: rendered security.txt
    :rtype: HttpResponse
    """

    context = {
        "SECURITY_TXT_ACKNOWLEDGMENTS": Acknowledgment.objects.all(),
        "SECURITY_TXT_CANONICALS": Canonical.objects.all(),
        "SECURITY_TXT_CONTACTS": Contact.objects.all(),
        "SECURITY_TXT_EXPIRES": settings.SECURITY_TXT_EXPIRES,
    }  # type: Dict[str, Union[Manager[Acknowledgment], Manager[Canonical], Manager[Contact], datetime]]  # noqa: E501

    return render(
        request=request,
        template_name="security_txt/security_txt.txt",
        context=context,
        content_type="text/plain; charset=utf-8",
    )
