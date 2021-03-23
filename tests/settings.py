# -*- coding: utf-8 -*-

# django-security-txt
# tests/settings.py


import sys
import random
import pathlib
from datetime import datetime
from typing import Dict, List, Union  # pylint: disable=W0611


# black magic to use imports from library code
sys.path.insert(0, str(pathlib.Path(__file__).absolute().parent.parent.parent))

# secret key
SECRET_KEY = "".join(
    [
        random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)")  # nosec
        for i in range(50)
    ]
)  # type: str

# configure databases
DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}
}  # type: Dict[str, Dict[str, str]]

# configure templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]  # type: List[Dict[str, Union[str, List[str], bool, Dict[str, Union[str, Dict[str, str], List[str]]]]]]  # noqa: E501


MIDDLEWARE = [
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
]  # type: List[str]

# add testing related apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django_nose",
    "phonenumber_field",
    "security_txt",
]  # type: List[str]

# add nose test runner
TEST_RUNNER = "django_nose.NoseTestSuiteRunner"  # type: str

# configure nose test runner
NOSE_ARGS = [
    "--rednose",
    "--force-color",
    "--with-timer",
    "--with-doctest",
    "--with-coverage",
    "--cover-inclusive",
    "--cover-erase",
    "--cover-package=security_txt",
    "--logging-clear-handlers",
]  # type: List[str]

# configure urls
ROOT_URLCONF = "security_txt.urls"  # type: str

# phone number settings
PHONENUMBER_DB_FORMAT = "INTERNATIONAL"

# security.txt settings
SECURITY_TXT_EXPIRES = datetime(year=1991, month=8, day=24)
