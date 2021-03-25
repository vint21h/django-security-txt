# -*- coding: utf-8 -*-

# django-security-txt
# tests/models/test_encryption.py


from typing import List  # pylint: disable=W0611

from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils.translation import override as override_translation

from security_txt.models.encryption import Encryption


__all__ = ["EncryptionModelTest"]  # type: List[str]


class EncryptionModelTest(TestCase):
    """
    Encryption model tests.
    """

    def test___unicode___type__url(self) -> None:
        """
        __unicode__ method must return URL.
        """

        encryption = Encryption.objects.create(
            type=Encryption.TYPE_URL, url="https://example.com/"
        )  # type: Encryption

        self.assertEqual(first=encryption.__unicode__(), second="https://example.com/")

    def test___unicode___type__dns(self) -> None:
        """
        __unicode__ method must return OPENPGPKEY DNS record.
        """

        encryption = Encryption.objects.create(
            type=Encryption.TYPE_DNS,
            dns="0123456789abcdef._openpgpkey.example.com?type=OPENPGPKEY",
        )  # type: Encryption

        self.assertEqual(
            first=encryption.__unicode__(),
            second="dns:0123456789abcdef._openpgpkey.example.com?type=OPENPGPKEY",
        )

    def test___unicode___type__fingerprint(self) -> None:
        """
        __unicode__ method must return OpenPGP key fingerprint.
        """

        encryption = Encryption.objects.create(
            type=Encryption.TYPE_FINGERPRINT,
            fingerprint="0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",  # noqa: E501
        )  # type: Encryption

        self.assertEqual(
            first=encryption.__unicode__(),
            second="openpgp4fpr:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",  # noqa: E501
        )

    def test___repr___type__url(self) -> None:
        """
        __repr__ method must return URL.
        """

        encryption = Encryption.objects.create(
            type=Encryption.TYPE_URL, url="https://example.com/"
        )  # type: Encryption

        self.assertEqual(first=encryption.__repr__(), second="https://example.com/")

    def test___repr___type__dns(self) -> None:
        """
        __repr__ method must return OPENPGPKEY DNS record.
        """

        encryption = Encryption.objects.create(
            type=Encryption.TYPE_DNS,
            dns="0123456789abcdef._openpgpkey.example.com?type=OPENPGPKEY",
        )  # type: Encryption

        self.assertEqual(
            first=encryption.__repr__(),
            second="dns:0123456789abcdef._openpgpkey.example.com?type=OPENPGPKEY",
        )

    def test___repr___type__fingerprint(self) -> None:
        """
        __repr__ method must return OpenPGP key fingerprint.
        """

        encryption = Encryption.objects.create(
            type=Encryption.TYPE_FINGERPRINT,
            fingerprint="0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",  # noqa: E501
        )  # type: Encryption

        self.assertEqual(
            first=encryption.__repr__(),
            second="openpgp4fpr:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",  # noqa: E501
        )

    def test___str___type__url(self) -> None:
        """
        __str__ method must return URL.
        """

        encryption = Encryption.objects.create(
            type=Encryption.TYPE_URL, url="https://example.com/"
        )  # type: Encryption

        self.assertEqual(first=encryption.__str__(), second="https://example.com/")

    def test___str___type__dns(self) -> None:
        """
        __str__ method must return OPENPGPKEY DNS record.
        """

        encryption = Encryption.objects.create(
            type=Encryption.TYPE_DNS,
            dns="0123456789abcdef._openpgpkey.example.com?type=OPENPGPKEY",
        )  # type: Encryption

        self.assertEqual(
            first=encryption.__str__(),
            second="dns:0123456789abcdef._openpgpkey.example.com?type=OPENPGPKEY",
        )

    def test___str___type__fingerprint(self) -> None:
        """
        __str__ method must return OpenPGP key fingerprint.
        """

        encryption = Encryption.objects.create(
            type=Encryption.TYPE_FINGERPRINT,
            fingerprint="0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",  # noqa: E501
        )  # type: Encryption

        self.assertEqual(
            first=encryption.__str__(),
            second="openpgp4fpr:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",  # noqa: E501
        )

    @override_translation(language="en")
    def test_clean(self) -> None:
        """
        clean method must raise validation error on bad contact type and value field combination.
        """  # noqa: E501

        with self.assertRaises(
            expected_exception=ValidationError,
            msg="",
        ):
            encryption = Encryption(
                type=Encryption.TYPE_DNS, url="https://example.com/"
            )  # type: Encryption
            encryption.clean()
