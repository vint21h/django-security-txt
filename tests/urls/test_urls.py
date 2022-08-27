# -*- coding: utf-8 -*-

# django-security-txt
# tests/test_views.py


from typing import List

from django.test import TestCase
from http import HTTPStatus

__all__: List[str] = ["URLTest"]

class URLTest(TestCase):
    """ test urls.py """

    def test_url(self) -> None:
        """ Test status_code and content_type """
        response = self.client.get("/")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response["content-type"], "text/plain")
