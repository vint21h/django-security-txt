# -*- coding: utf-8 -*-

# django-security-txt
# tests/models/test_policy.py


from typing import List, Optional

from django.test import TestCase

from security_txt.models.policy import Policy


__all__: List[str] = ["PolicyModelTest"]


class PolicyModelTest(TestCase):
    """Policy model tests."""

    @classmethod
    def setUpTestData(cls) -> None:
        """Set up non-modified objects used by all test methods."""
        Policy.objects.create(url="https://example.com/")

    def test___unicode__(self) -> None:
        """__unicode__ method must return policy URL."""
        policy: Optional[Policy] = Policy.objects.first()

        self.assertEqual(
            first=policy.__unicode__(), second="https://example.com/"  # type: ignore
        )

    def test___repr__(self) -> None:
        """__repr__ method must return policy URL."""
        policy: Optional[Policy] = Policy.objects.first()

        self.assertEqual(first=policy.__repr__(), second="https://example.com/")

    def test___str__(self) -> None:
        """__str__ method must return policy URL."""
        policy: Optional[Policy] = Policy.objects.first()

        self.assertEqual(first=policy.__str__(), second="https://example.com/")
