# -*- coding: utf-8 -*-

# django-security-txt
# tests/checks/test_system_checks.py


from typing import List

from django.test import TestCase
from django.test.utils import override_settings
from django.urls import reverse

from pathlib import Path
from tempfile import NamedTemporaryFile
from pgpy import PGPUID, PGPKey
from pgpy.constants import (
    KeyFlags,
    HashAlgorithm,
    PubKeyAlgorithm,
    CompressionAlgorithm,
    SymmetricKeyAlgorithm,
)

from security_txt.checks import EXPIRY_DATE_WARNING, KEY_NOT_VALID_ERROR, NO_CONTACT_WARNING, check_for_expiration_date, check_for_min_one_contact, check_if_key_exists_n_valid
from security_txt.models.contact import Contact

__all__: List[str] = ["SecurityTxtCheckTest"]


KEY_PATH: str = NamedTemporaryFile().name

class SecurityTxtCheckTest(TestCase):
    """Test all the system checks."""

    @override_settings(SECURITY_TXT_SIGN=False)
    def test_no_sign_no_key(self):
        self.assertListEqual(check_if_key_exists_n_valid(), [])

    @override_settings(SECURITY_TXT_SIGN=True)
    def test_sign_no_key(self):
        self.assertListEqual(check_if_key_exists_n_valid(), [KEY_NOT_VALID_ERROR])
    
    @override_settings(SECURITY_TXT_SIGN=True, SECURITY_TXT_SIGNING_KEY=KEY_PATH)
    def test_sign_w_key(self):
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
        Path(KEY_PATH).write_text(data=str(key))

        self.assertListEqual(check_if_key_exists_n_valid(), [])
    
    def test_min_one_contact_warning(self):
        self.assertListEqual(check_for_min_one_contact(), [NO_CONTACT_WARNING])
        Contact.objects.create(email="test@example.com")
        self.assertListEqual(check_for_min_one_contact(), [])

    def test_expiry_date_warning(self):
        self.assertListEqual(check_for_expiration_date(), [EXPIRY_DATE_WARNING])

    def test_check_root_url_correct(self):
        # url = reverse('security-txt:SecurityTxtView')
        # import pdb; pdb.set_trace()
        # TODO:
        pass

    def test_check_root_url_not_correct(self):
        # TODO:
        pass
