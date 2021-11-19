# -*- coding: utf-8 -*-

# django-security-txt
# tests/models/test_acknowledgment.py


from typing import List, Optional

from django.test import TestCase

from security_txt.models.acknowledgment import Acknowledgment


__all__: List[str] = ["AcknowledgmentModelTest"]


class AcknowledgmentModelTest(TestCase):
    """Acknowledgment model tests."""

    @classmethod
    def setUpTestData(cls) -> None:
        """Set up non-modified objects used by all test methods."""
        Acknowledgment.objects.create(url="https://example.com/")

    def test___unicode__(self) -> None:
        """__unicode__ method must return acknowledgments URL."""
        acknowledgment: Optional[Acknowledgment] = (
            Acknowledgment.objects.first()
        )

        self.assertEqual(
            first=acknowledgment.__unicode__(), second="https://example.com/"  # type: ignore  # noqa: E501
        )

    def test___repr__(self) -> None:
        """__repr__ method must return acknowledgments URL."""
        acknowledgment: Optional[Acknowledgment] = (
            Acknowledgment.objects.first()
        )

        self.assertEqual(first=acknowledgment.__repr__(), second="https://example.com/")

    def test___str__(self) -> None:
        """__str__ method must return acknowledgments URL."""
        acknowledgment: Optional[Acknowledgment] = (
            Acknowledgment.objects.first()
        )

        self.assertEqual(first=acknowledgment.__str__(), second="https://example.com/")
