# -*- coding: utf-8 -*-

# django-security-txt
# tests/models/test_canonical.py


from typing import List, Optional  # pylint: disable=W0611

from django.test import TestCase

from security_txt.models.canonical import Canonical


__all__ = ["CanonicalModelTest"]  # type: List[str]


class CanonicalModelTest(TestCase):
    """
    Canonical model tests.
    """

    @classmethod
    def setUpTestData(cls) -> None:
        """
        Set up non-modified objects used by all test methods.
        """

        Canonical.objects.create(url="https://example.com/.well-known/security.txt")

    def test___unicode__(self) -> None:
        """
        __unicode__ method must return canonical URL.
        """

        canonical = Canonical.objects.first()  # type: Optional[Canonical]

        self.assertEqual(
            first=canonical.__unicode__(),  # type: ignore
            second="https://example.com/.well-known/security.txt",
        )

    def test___repr__(self) -> None:
        """
        __repr__ method must return canonical URL.
        """

        canonical = Canonical.objects.first()  # type: Optional[Canonical]

        self.assertEqual(
            first=canonical.__repr__(),
            second="https://example.com/.well-known/security.txt",
        )

    def test___str__(self) -> None:
        """
        __str__ method must return canonical URL.
        """

        canonical = Canonical.objects.first()  # type: Optional[Canonical]

        self.assertEqual(
            first=canonical.__str__(),
            second="https://example.com/.well-known/security.txt",
        )
