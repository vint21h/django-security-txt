# -*- coding: utf-8 -*-

# django-security-txt
# tests/settings.py


import sys
import pathlib
from datetime import datetime
from random import SystemRandom
from typing import Any, Dict, List


# black magic to use imports from library code
path = pathlib.Path(__file__).absolute()
project = path.parent.parent.parent
sys.path.insert(0, str(project))

# secret key
SECRET_KEY: str = "".join(
    [
        SystemRandom().choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)")
        for i in range(50)
    ]
)

# configure databases
DATABASES: Dict[str, Dict[str, str]] = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}
}

# configure templates
TEMPLATES: List[Dict[str, Any]] = [
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
]


MIDDLEWARE: List[str] = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
]

# add testing related apps
INSTALLED_APPS: List[str] = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "phonenumber_field",
    "security_txt",
]


# configure urls
ROOT_URLCONF: str = "security_txt.urls"

# phone number settings
PHONENUMBER_DB_FORMAT: str = "INTERNATIONAL"

# security.txt settings
SECURITY_TXT_EXPIRES: datetime = datetime(
    year=1997, month=8, day=29, hour=2, minute=14
)
SECURITY_TXT_PREFERRED_LANGUAGES: List[str] = ["en", "uk"]

USE_TZ: bool = False
