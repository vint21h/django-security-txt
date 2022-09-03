# -*- coding: utf-8 -*-

# django-security-txt
# tests/views/test_signed_security_txt_views.py


from typing import List
from pathlib import Path
from http.client import HTTPResponse
from tempfile import NamedTemporaryFile

from pgpy import PGPUID, PGPKey
from django.test import TestCase
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

from security_txt.views import signed_security_txt_data


__all__: List[str] = ["SignSecurityTxtViewTest"]

def generate_key_pair_in_tempfile(key_path: str) -> None:
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
    Path(key_path).write_text(data=str(key))



class SignSecurityTxtViewTest(TestCase):
    """Sign security.txt templatetag tests."""

    KEY_PATH = NamedTemporaryFile().name

    @override_translation("en")
    @override_settings(SECURITY_TXT_SIGN=True, SECURITY_TXT_SIGNING_KEY=KEY_PATH)
    def test_sign_security_txt__non_valid_key(self) -> None:
        """Test templatetag returning response."""
        with self.assertRaises(expected_exception=ImproperlyConfigured):
            signed_security_txt_data("")

    @override_translation("en")
    @override_settings(SECURITY_TXT_SIGN=True, SECURITY_TXT_SIGNING_KEY=KEY_PATH)
    def test_sign_security_txt__render(self) -> None:
        """Test templatetag rendering result."""
        expected_list: List[bytes] = [
            b"-----BEGIN PGP SIGNED MESSAGE-----",
            b"Hash: SHA256",
            b"-----BEGIN PGP SIGNATURE-----"
        ]
        generate_key_pair_in_tempfile(self.KEY_PATH)
        response: HTTPResponse = self.client.get("/")
        result: bytes = response.content
        for expected in expected_list:
            self.assertTrue(expr=expected in result)

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
