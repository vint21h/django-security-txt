# -*- coding: utf-8 -*-

# django-security-txt
# tests/models/test_contact.py


from typing import List  # pylint: disable=W0611

from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils.translation import override as override_translation

from security_txt.models.contact import Contact


__all__ = ["ContactModelTest"]  # type: List[str]


class ContactModelTest(TestCase):
    """
    Contact model tests.
    """

    def test___unicode___type__email(self) -> None:
        """
        __unicode__ method must return contact e-mail.
        """

        contact = Contact.objects.create(
            type=Contact.TYPE_EMAIL, email="test@example.com"
        )  # type: Contact

        self.assertEqual(first=contact.__unicode__(), second="mailto:test@example.com")

    def test___unicode___type__phone(self) -> None:
        """
        __unicode__ method must return contact phone.
        """

        contact = Contact.objects.create(
            type=Contact.TYPE_PHONE, phone="+380441234567"
        )  # type: Contact

        self.assertEqual(first=contact.__unicode__(), second="tel:+380441234567")

    def test___unicode___type__url(self) -> None:
        """
        __unicode__ method must return contact URL.
        """

        contact = Contact.objects.create(
            type=Contact.TYPE_URL, url="https://example.com"
        )  # type: Contact

        self.assertEqual(first=contact.__unicode__(), second="https://example.com")

    def test___repr___type__email(self) -> None:
        """
        __repr__ method must return contact e-mail.
        """

        contact = Contact.objects.create(
            type=Contact.TYPE_EMAIL, email="test@example.com"
        )  # type: Contact

        self.assertEqual(first=contact.__repr__(), second="mailto:test@example.com")

    def test___repr___type__phone(self) -> None:
        """
        __repr__ method must return contact phone.
        """

        contact = Contact.objects.create(
            type=Contact.TYPE_PHONE, phone="+380441234567"
        )  # type: Contact

        self.assertEqual(first=contact.__repr__(), second="tel:+380441234567")

    def test___repr___type__url(self) -> None:
        """
        __repr__ method must return contact URL.
        """

        contact = Contact.objects.create(
            type=Contact.TYPE_URL, url="https://example.com"
        )  # type: Contact

        self.assertEqual(first=contact.__repr__(), second="https://example.com")

    def test___str___type__email(self) -> None:
        """
        __str__ method must return contact e-mail.
        """

        contact = Contact.objects.create(
            type=Contact.TYPE_EMAIL, email="test@example.com"
        )  # type: Contact

        self.assertEqual(first=contact.__str__(), second="mailto:test@example.com")

    def test___str___type__phone(self) -> None:
        """
        __str__ method must return contact phone.
        """

        contact = Contact.objects.create(
            type=Contact.TYPE_PHONE, phone="+380441234567"
        )  # type: Contact

        self.assertEqual(first=contact.__str__(), second="tel:+380441234567")

    def test___str___type__url(self) -> None:
        """
        __str__ method must return contact URL.
        """

        contact = Contact.objects.create(
            type=Contact.TYPE_URL, url="https://example.com"
        )  # type: Contact

        self.assertEqual(first=contact.__str__(), second="https://example.com")

    @override_translation(language="en")
    def test_clean(self) -> None:
        """
        clean method must raise validation error on bad contact type and value field combination.
        """  # noqa: E501

        with self.assertRaises(
            expected_exception=ValidationError,
            msg="",
        ):
            contact = Contact(
                type=Contact.TYPE_EMAIL, url="https://example.com"
            )  # type: Contact
            contact.clean()
