# -*- coding: utf-8 -*-

# django-security-txt
# tests/test_views.py


from typing import List
from http import HTTPStatus

from django.test import TestCase

from security_txt.models.contact import Contact
from security_txt.models.acknowledgment import Acknowledgment


__all__: List[str] = ["URLTest"]


class URLTest(TestCase):
    """test urls.py."""

    @classmethod
    def setUpTestData(cls) -> None:
        """Set up non-modified objects used by all test methods."""
        Acknowledgment.objects.create(url="https://example.com/")
        Contact.objects.create(
            type=Contact.TYPE_EMAIL, email="test@example.com"
        )

    def test_url(self) -> None:
        """Test status_code and content_type."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response["content-type"], "text/plain")
        self.assertContains(response, "test@example.com")
        self.assertContains(response, "https://example.com")
