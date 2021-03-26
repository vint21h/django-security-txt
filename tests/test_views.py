# -*- coding: utf-8 -*-

# django-security-txt
# tests/test_views.py


from typing import List  # pylint: disable=W0611

from django.test import TestCase
from django.shortcuts import resolve_url
from django.test.utils import override_settings
from django.http import HttpRequest, HttpResponse
from django.utils.translation import override as override_translation

from security_txt.views import security_txt
from security_txt.models.hiring import Hiring
from security_txt.models.policy import Policy
from security_txt.models.contact import Contact
from security_txt.models.canonical import Canonical
from security_txt.models.encryption import Encryption
from security_txt.models.acknowledgment import Acknowledgment


__all__ = ["SecurityTxtViewTest"]  # type: List[str]


class SecurityTxtViewTest(TestCase):
    """
    security.txt view tests.
    """

    @classmethod
    def setUpTestData(cls) -> None:
        """
        Set up non-modified objects used by all test methods.
        """

        Acknowledgment.objects.create(url="https://example.com/")
        Canonical.objects.create(url="https://example.com/.well-known/security.txt")
        Canonical.objects.create(url="https://www.example.com/.well-known/security.txt")
        Contact.objects.create(type=Contact.TYPE_EMAIL, email="test@example.com")
        Contact.objects.create(type=Contact.TYPE_PHONE, phone="+380441234567")
        Contact.objects.create(type=Contact.TYPE_URL, url="https://example.com")
        Encryption.objects.create(type=Encryption.TYPE_URL, url="https://example.com/")
        Encryption.objects.create(
            type=Encryption.TYPE_DNS,
            dns="0123456789abcdef._openpgpkey.example.com?type=OPENPGPKEY",
        )
        Encryption.objects.create(
            type=Encryption.TYPE_FINGERPRINT,
            fingerprint="0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",  # noqa: E501
        )
        Hiring.objects.create(url="https://example.com/")
        Policy.objects.create(url="https://example.com/")

    def test_security_txt__return_response(self) -> None:
        """
        Test view returning response.
        """

        request = HttpRequest()  # type: HttpRequest

        self.assertIsInstance(obj=security_txt(request=request), cls=HttpResponse)

    @override_translation("en")
    def test_security_txt__render__template_used(self) -> None:
        """
        Test view right template usage.
        """

        result = self.client.get(
            path=resolve_url(to="security-txt")
        )  # type: HttpResponse

        self.assertTemplateUsed(
            response=result, template_name="security_txt/security_txt.txt"
        )

    @override_translation("en")
    def test_security_txt__render(self) -> None:
        """
        Test view rendering result.
        """

        expected = """
        # Our security acknowledgments page
        Acknowledgments: https://example.com/
        # Canonical URI
        Canonical: https://example.com/.well-known/security.txt
        Canonical: https://www.example.com/.well-known/security.txt
        # Our security address
        Contact: mailto:test@example.com
        Contact: tel:+380441234567
        Contact: https://example.com
        # Our OpenPGP key
        Encryption: https://example.com/
        Encryption: dns:0123456789abcdef._openpgpkey.example.com?type=OPENPGPKEY
        Encryption: openpgp4fpr:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
        Expires: Aug. 29, 1997, 2:14 a.m.
        Hiring: https://example.com/
        # Our security policy
        Policy: https://example.com/
        Preferred-Languages: en, uk
        """  # type: str  # noqa: E501
        result = self.client.get(
            path=resolve_url(to="security-txt")
        )  # type: HttpResponse

        self.assertIsNotNone(
            obj=result.context.get("SECURITY_TXT_ACKNOWLEDGMENTS")
            if result.context
            else None
        )
        self.assertIsNotNone(
            obj=result.context.get("SECURITY_TXT_CANONICALS")
            if result.context
            else None
        )
        self.assertIsNotNone(
            obj=result.context.get("SECURITY_TXT_CONTACTS") if result.context else None
        )
        self.assertIsNotNone(
            obj=result.context.get("SECURITY_TXT_ENCRYPTION")
            if result.context
            else None
        )
        self.assertIsNotNone(
            obj=result.context.get("SECURITY_TXT_EXPIRES") if result.context else None
        )
        self.assertIsNotNone(
            obj=result.context.get("SECURITY_TXT_HIRING") if result.context else None
        )
        self.assertIsNotNone(
            obj=result.context.get("SECURITY_TXT_POLICIES") if result.context else None
        )
        self.assertIsNotNone(
            obj=result.context.get("SECURITY_TXT_PREFERRED_LANGUAGES")
            if result.context
            else None
        )
        self.assertHTMLEqual(html1=result.content.decode(), html2=expected)

    @override_translation("en")
    @override_settings(SECURITY_TXT_EXPIRES=None)
    def test_security_txt__render__without_expires(self) -> None:
        """
        Test view rendering result without expires date/time.
        """

        expected = """
        # Our security acknowledgments page
        Acknowledgments: https://example.com/
        # Canonical URI
        Canonical: https://example.com/.well-known/security.txt
        Canonical: https://www.example.com/.well-known/security.txt
        # Our security address
        Contact: mailto:test@example.com
        Contact: tel:+380441234567
        Contact: https://example.com
        # Our OpenPGP key
        Encryption: https://example.com/
        Encryption: dns:0123456789abcdef._openpgpkey.example.com?type=OPENPGPKEY
        Encryption: openpgp4fpr:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
        Hiring: https://example.com/
        # Our security policy
        Policy: https://example.com/
        Preferred-Languages: en, uk
        """  # type: str  # noqa: E501
        result = self.client.get(
            path=resolve_url(to="security-txt")
        )  # type: HttpResponse

        self.assertIsNone(
            obj=result.context.get("SECURITY_TXT_EXPIRES") if result.context else None
        )
        self.assertHTMLEqual(html1=result.content.decode(), html2=expected)

    @override_translation("en")
    @override_settings(SECURITY_TXT_PREFERRED_LANGUAGES=None)
    def test_security_txt__render__without_preferred_languages(self) -> None:
        """
        Test view rendering result without preferred languages.
        """

        expected = """
        # Our security acknowledgments page
        Acknowledgments: https://example.com/
        # Canonical URI
        Canonical: https://example.com/.well-known/security.txt
        Canonical: https://www.example.com/.well-known/security.txt
        # Our security address
        Contact: mailto:test@example.com
        Contact: tel:+380441234567
        Contact: https://example.com
        # Our OpenPGP key
        Encryption: https://example.com/
        Encryption: dns:0123456789abcdef._openpgpkey.example.com?type=OPENPGPKEY
        Encryption: openpgp4fpr:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
        Expires: Aug. 29, 1997, 2:14 a.m.
        Hiring: https://example.com/
        # Our security policy
        Policy: https://example.com/
        """  # type: str  # noqa: E501
        result = self.client.get(
            path=resolve_url(to="security-txt")
        )  # type: HttpResponse

        self.assertIsNone(
            obj=result.context.get("SECURITY_TXT_PREFERRED_LANGUAGES")
            if result.context
            else None
        )
        self.assertHTMLEqual(html1=result.content.decode(), html2=expected)

    @override_translation("en")
    def test_security_txt__render__without_acknowledgments(self) -> None:
        """
        Test view rendering result without acknowledgments.
        """

        Acknowledgment.objects.all().delete()

        expected = """
        # Canonical URI
        Canonical: https://example.com/.well-known/security.txt
        Canonical: https://www.example.com/.well-known/security.txt
        # Our security address
        Contact: mailto:test@example.com
        Contact: tel:+380441234567
        Contact: https://example.com
        # Our OpenPGP key
        Encryption: https://example.com/
        Encryption: dns:0123456789abcdef._openpgpkey.example.com?type=OPENPGPKEY
        Encryption: openpgp4fpr:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
        Expires: Aug. 29, 1997, 2:14 a.m.
        Hiring: https://example.com/
        # Our security policy
        Policy: https://example.com/
        Preferred-Languages: en, uk
        """  # type: str  # noqa: E501
        result = self.client.get(
            path=resolve_url(to="security-txt")
        )  # type: HttpResponse

        self.assertQuerysetEqual(
            qs=result.context.get(  # type: ignore
                "SECURITY_TXT_ACKNOWLEDGMENTS", Acknowledgment.objects.none()
            )
            if result.context
            else Acknowledgment.objects.none(),
            values=Acknowledgment.objects.none(),
        )
        self.assertHTMLEqual(html1=result.content.decode(), html2=expected)

    @override_translation("en")
    def test_security_txt__render__without_canonicals(self) -> None:
        """
        Test view rendering result without canonicals.
        """

        Canonical.objects.all().delete()

        expected = """
        # Our security acknowledgments page
        Acknowledgments: https://example.com/
        # Our security address
        Contact: mailto:test@example.com
        Contact: tel:+380441234567
        Contact: https://example.com
        # Our OpenPGP key
        Encryption: https://example.com/
        Encryption: dns:0123456789abcdef._openpgpkey.example.com?type=OPENPGPKEY
        Encryption: openpgp4fpr:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
        Expires: Aug. 29, 1997, 2:14 a.m.
        Hiring: https://example.com/
        # Our security policy
        Policy: https://example.com/
        Preferred-Languages: en, uk
        """  # type: str  # noqa: E501
        result = self.client.get(
            path=resolve_url(to="security-txt")
        )  # type: HttpResponse

        self.assertQuerysetEqual(
            qs=result.context.get(  # type: ignore
                "SECURITY_TXT_CANONICALS", Canonical.objects.none()
            )
            if result.context
            else Canonical.objects.none(),
            values=Canonical.objects.none(),
        )
        self.assertHTMLEqual(html1=result.content.decode(), html2=expected)

    @override_translation("en")
    def test_security_txt__render__without_contacts(self) -> None:
        """
        Test view rendering result without contacts.
        """

        Contact.objects.all().delete()

        expected = """
        # Our security acknowledgments page
        Acknowledgments: https://example.com/
        # Canonical URI
        Canonical: https://example.com/.well-known/security.txt
        Canonical: https://www.example.com/.well-known/security.txt
        # Our OpenPGP key
        Encryption: https://example.com/
        Encryption: dns:0123456789abcdef._openpgpkey.example.com?type=OPENPGPKEY
        Encryption: openpgp4fpr:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
        Expires: Aug. 29, 1997, 2:14 a.m.
        Hiring: https://example.com/
        # Our security policy
        Policy: https://example.com/
        Preferred-Languages: en, uk
        """  # type: str  # noqa: E501
        result = self.client.get(
            path=resolve_url(to="security-txt")
        )  # type: HttpResponse

        self.assertQuerysetEqual(
            qs=result.context.get(  # type: ignore
                "SECURITY_TXT_CONTACTS", Contact.objects.none()
            )
            if result.context
            else Contact.objects.none(),
            values=Contact.objects.none(),
        )
        self.assertHTMLEqual(html1=result.content.decode(), html2=expected)

    @override_translation("en")
    def test_security_txt__render__without_encryption(self) -> None:
        """
        Test view rendering result without encryption.
        """

        Encryption.objects.all().delete()

        expected = """
        # Our security acknowledgments page
        Acknowledgments: https://example.com/
        # Canonical URI
        Canonical: https://example.com/.well-known/security.txt
        Canonical: https://www.example.com/.well-known/security.txt
        # Our security address
        Contact: mailto:test@example.com
        Contact: tel:+380441234567
        Contact: https://example.com
        Expires: Aug. 29, 1997, 2:14 a.m.
        Hiring: https://example.com/
        # Our security policy
        Policy: https://example.com/
        Preferred-Languages: en, uk
        """  # type: str  # noqa: E501
        result = self.client.get(
            path=resolve_url(to="security-txt")
        )  # type: HttpResponse

        self.assertQuerysetEqual(
            qs=result.context.get(  # type: ignore
                "SECURITY_TXT_ENCRYPTION", Encryption.objects.none()
            )
            if result.context
            else Encryption.objects.none(),
            values=Encryption.objects.none(),
        )
        self.assertHTMLEqual(html1=result.content.decode(), html2=expected)

    @override_translation("en")
    def test_security_txt__render__without_hiring(self) -> None:
        """
        Test view rendering result without hiring.
        """

        Hiring.objects.all().delete()

        expected = """
        # Our security acknowledgments page
        Acknowledgments: https://example.com/
        # Canonical URI
        Canonical: https://example.com/.well-known/security.txt
        Canonical: https://www.example.com/.well-known/security.txt
        # Our security address
        Contact: mailto:test@example.com
        Contact: tel:+380441234567
        Contact: https://example.com
        # Our OpenPGP key
        Encryption: https://example.com/
        Encryption: dns:0123456789abcdef._openpgpkey.example.com?type=OPENPGPKEY
        Encryption: openpgp4fpr:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
        Expires: Aug. 29, 1997, 2:14 a.m.
        # Our security policy
        Policy: https://example.com/
        Preferred-Languages: en, uk
        """  # type: str  # noqa: E501
        result = self.client.get(
            path=resolve_url(to="security-txt")
        )  # type: HttpResponse

        self.assertQuerysetEqual(
            qs=result.context.get(  # type: ignore
                "SECURITY_TXT_HIRING", Hiring.objects.none()
            )
            if result.context
            else Hiring.objects.none(),
            values=Hiring.objects.none(),
        )
        self.assertHTMLEqual(html1=result.content.decode(), html2=expected)

    @override_translation("en")
    def test_security_txt__render__without_policies(self) -> None:
        """
        Test view rendering result without policies.
        """

        Policy.objects.all().delete()

        expected = """
        # Our security acknowledgments page
        Acknowledgments: https://example.com/
        # Canonical URI
        Canonical: https://example.com/.well-known/security.txt
        Canonical: https://www.example.com/.well-known/security.txt
        # Our security address
        Contact: mailto:test@example.com
        Contact: tel:+380441234567
        Contact: https://example.com
        # Our OpenPGP key
        Encryption: https://example.com/
        Encryption: dns:0123456789abcdef._openpgpkey.example.com?type=OPENPGPKEY
        Encryption: openpgp4fpr:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
        Expires: Aug. 29, 1997, 2:14 a.m.
        Hiring: https://example.com/
        Preferred-Languages: en, uk
        """  # type: str  # noqa: E501
        result = self.client.get(
            path=resolve_url(to="security-txt")
        )  # type: HttpResponse

        self.assertQuerysetEqual(
            qs=result.context.get(  # type: ignore
                "SECURITY_TXT_POLICIES", Policy.objects.none()
            )
            if result.context
            else Policy.objects.none(),
            values=Policy.objects.none(),
        )
        self.assertHTMLEqual(html1=result.content.decode(), html2=expected)
