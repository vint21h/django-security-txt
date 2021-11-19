# -*- coding: utf-8 -*-

# django-security-txt
# tests/models/test_hiring.py


from typing import List, Optional

from django.test import TestCase

from security_txt.models.hiring import Hiring


__all__: List[str] = ["HiringModelTest"]


class HiringModelTest(TestCase):
    """Hiring model tests."""

    @classmethod
    def setUpTestData(cls) -> None:
        """Set up non-modified objects used by all test methods."""
        Hiring.objects.create(url="https://example.com/")

    def test___unicode__(self) -> None:
        """__unicode__ method must return hiring URL."""
        hiring: Optional[Hiring] = Hiring.objects.first()

        self.assertEqual(
            first=hiring.__unicode__(), second="https://example.com/"  # type: ignore
        )

    def test___repr__(self) -> None:
        """__repr__ method must return hiring URL."""
        hiring: Optional[Hiring] = Hiring.objects.first()

        self.assertEqual(first=hiring.__repr__(), second="https://example.com/")

    def test___str__(self) -> None:
        """__str__ method must return hiring URL."""
        hiring: Optional[Hiring] = Hiring.objects.first()

        self.assertEqual(first=hiring.__str__(), second="https://example.com/")
