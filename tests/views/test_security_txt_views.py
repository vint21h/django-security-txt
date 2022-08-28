# -*- coding: utf-8 -*-

# django-security-txt
# tests/test_views.py


from typing import List
from pathlib import Path
from tempfile import NamedTemporaryFile
from unittest import skip

from pgpy import PGPUID, PGPKey
from django.test import TestCase
from django.template import Context, Template
from django.test.utils import override_settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import override as override_translation
from pgpy.constants import (
    KeyFlags,
    HashAlgorithm,
    PubKeyAlgorithm,
    CompressionAlgorithm,
    SymmetricKeyAlgorithm,
)

from security_txt.models.hiring import Hiring
from security_txt.models.policy import Policy
from security_txt.models.contact import Contact
from security_txt.models.canonical import Canonical
from security_txt.models.encryption import Encryption
from security_txt.models.acknowledgment import Acknowledgment

from security_txt.views import get_security_txt_data, get_security_txt_lines_by_model, signed_security_txt_data


__all__: List[str] = ["SecurityTxtViewTest"]


class SecurityTxtViewTest(TestCase):
    """security.txt view tests."""

    @classmethod
    def setUpTestData(cls) -> None:
        """Set up non-modified objects used by all test methods."""
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

    def test_security_txt_data__return_response(self) -> None:
        """Test templatetag returning response."""
        self.assertIsInstance(obj=get_security_txt_data(), cls=str)

    @override_translation("en")
    def test_security_txt__render(self) -> None:
        """Test templatetag rendering result."""
        expected: bytes = \
b"""# Our security acknowledgments page
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
Expires: 1997-08-29T02:14:00
Hiring: https://example.com/
# Our security policy
Policy: https://example.com/
Preferred-Languages: en, uk"""  # noqa: E50

        result = self.client.get("/")
        self.assertEqual(result.content, expected)

    @override_translation("en")
    @override_settings(SECURITY_TXT_EXPIRES=None)
    def test_security_txt__render__without_expires(self) -> None:
        """Test view rendering result without expires date/time."""
        expected: str = \
b"""# Our security acknowledgments page
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
Expires: 
Hiring: https://example.com/
# Our security policy
Policy: https://example.com/
Preferred-Languages: en, uk"""  # noqa: E501
        result = self.client.get("/")
        self.assertEqual(result.content, expected)

    @override_translation("en")
    @override_settings(SECURITY_TXT_PREFERRED_LANGUAGES=None)
    def test_security_txt__render__without_preferred_languages(self) -> None:
        """Test view rendering result without preferred languages."""
        expected: str = \
b"""# Our security acknowledgments page
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
Expires: 1997-08-29T02:14:00
Hiring: https://example.com/
# Our security policy
Policy: https://example.com/"""  # noqa: E501
        result = self.client.get("/")
        self.assertEqual(result.content, expected)

    @override_translation("en")
    def test_security_txt__render__without_acknowledgments(self) -> None:
        """Test view rendering result without acknowledgments."""
        Acknowledgment.objects.all().delete()

        expected: str = """
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
        """  # noqa: E501
        template: Template = Template(
            "{% load security_txt_tags %}" "{% security_txt %}"  # noqa: FS003
        )
        result: str = template.render(context=Context())

        self.assertHTMLEqual(html1=result, html2=expected)

    @override_translation("en")
    def test_security_txt__render__without_canonicals(self) -> None:
        """Test view rendering result without canonicals."""
        Canonical.objects.all().delete()

        expected: str = """
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
        """  # noqa: E501
        template: Template = Template(
            "{% load security_txt_tags %}" "{% security_txt %}"  # noqa: FS003
        )
        result: str = template.render(context=Context())

        self.assertHTMLEqual(html1=result, html2=expected)

    @override_translation("en")
    def test_security_txt__render__without_contacts(self) -> None:
        """Test view rendering result without contacts."""
        Contact.objects.all().delete()

        expected: str = """
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
        """  # noqa: E501
        template: Template = Template(
            "{% load security_txt_tags %}" "{% security_txt %}"  # noqa: FS003
        )
        result: str = template.render(context=Context())

        self.assertHTMLEqual(html1=result, html2=expected)

    @override_translation("en")
    def test_security_txt__render__without_encryption(self) -> None:
        """Test view rendering result without encryption."""
        Encryption.objects.all().delete()

        expected: str = """
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
        """  # noqa: E501
        template: Template = Template(
            "{% load security_txt_tags %}" "{% security_txt %}"  # noqa: FS003
        )
        result: str = template.render(context=Context())

        self.assertHTMLEqual(html1=result, html2=expected)

    @override_translation("en")
    def test_security_txt__render__without_hiring(self) -> None:
        """Test view rendering result without hiring."""
        Hiring.objects.all().delete()

        expected: str = """
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
        """  # noqa: E501
        template: Template = Template(
            "{% load security_txt_tags %}" "{% security_txt %}"  # noqa: FS003
        )
        result: str = template.render(context=Context())

        self.assertHTMLEqual(html1=result, html2=expected)

    @override_translation("en")
    def test_security_txt__render__without_policies(self) -> None:
        """Test view rendering result without policies."""
        Policy.objects.all().delete()

        expected: str = """
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
        """  # noqa: E501
        template: Template = Template(
            "{% load security_txt_tags %}" "{% security_txt %}"  # noqa: FS003
        )
        result: str = template.render(context=Context())

        self.assertHTMLEqual(html1=result, html2=expected)


class SignSecurityTxtTemplatetagTest(TestCase):
    """Sign security.txt templatetag tests."""

    KEY_PATH = NamedTemporaryFile().name

    @skip("KEY_PATH has to be a valid key")
    @override_translation("en")
    @override_settings(SECURITY_TXT_SIGN=True, SECURITY_TXT_SIGNING_KEY=KEY_PATH)
    def test_sign_security_txt__return_response(self) -> None:
        """Test templatetag returning response."""
        self.assertIsInstance(obj=signed_security_txt_data(""), cls=str)

    @override_translation("en")
    @override_settings(SECURITY_TXT_SIGN=True, SECURITY_TXT_SIGNING_KEY=KEY_PATH)
    def test_sign_security_txt__render(self) -> None:
        """Test templatetag rendering result."""
        expected = """
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

-----BEGIN PGP SIGNATURE-----
        """
        template: Template = Template(
            "{% load security_txt_tags %}"  # noqa: FS003
            "{% with security_txt as DATA %}{% sign_security_txt DATA %}{% endwith %}"  # noqa: FS003,E501
        )
        key = PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 4096)
        uid = PGPUID.new(pn="TEST", comment="Test", email="test@example.com")
        key.add_uid(
            uid,
            usage={
                KeyFlags.Sign,
                KeyFlags.EncryptCommunications,
                KeyFlags.EncryptStorage,
            },
            hashes=[
                HashAlgorithm.SHA256,
                HashAlgorithm.SHA384,
                HashAlgorithm.SHA512,
                HashAlgorithm.SHA224,
            ],
            ciphers=[
                SymmetricKeyAlgorithm.AES256,
                SymmetricKeyAlgorithm.AES192,
                SymmetricKeyAlgorithm.AES128,
            ],
            compression=[
                CompressionAlgorithm.ZLIB,
                CompressionAlgorithm.BZ2,
                CompressionAlgorithm.ZIP,
                CompressionAlgorithm.Uncompressed,
            ],
        )
        Path(self.KEY_PATH).write_text(data=str(key))
        result: str = template.render(context=Context())

        self.assertTrue(expr=expected.strip() in result.strip())

    @override_translation("en")
    @override_settings(SECURITY_TXT_SIGN=True, SECURITY_TXT_SIGNING_KEY="")
    def test_sign_security_txt__improperly_configured(self) -> None:
        """Test templatetag raises improperly configured error."""
        with self.assertRaises(expected_exception=ImproperlyConfigured, msg=""):
            signed_security_txt_data("")

    @override_translation("en")
    @override_settings(
        SECURITY_TXT_SIGN=True, SECURITY_TXT_SIGNING_KEY="/path/to/key.asc"
    )
    def test_sign_security_txt__improperly_configured__no_key(self) -> None:
        """Test templatetag raises improperly configured error for not existing key file."""  # noqa: E501
        with self.assertRaises(expected_exception=ImproperlyConfigured, msg=""):
            signed_security_txt_data("")
