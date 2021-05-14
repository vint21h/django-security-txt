.. django-security-txt
.. README.rst


A django-security-txt documentation
===================================

|GitHub|_ |Coveralls|_ |pypi-license|_ |pypi-version|_ |pypi-python-version|_ |pypi-django-version|_ |pypi-format|_ |pypi-wheel|_ |pypi-status|_

    *django-security-txt is a Django reusable application to handle security.txt (http://securitytxt.org/)*

.. contents::

Installation
------------
* Obtain your copy of source code from the git repository: ``$ git clone https://github.com/vint21h/django-security-txt.git``. Or download the latest release from https://github.com/vint21h/django-security-txt/tags/.
* Run ``$ python ./setup.py install`` from the repository source tree or the unpacked archive. Or use pip: ``$ pip install django-security-txt``.

Configuration
-------------
* Add ``"security_txt"`` to ``settings.INSTALLED_APPS``:

.. code-block:: python

    # settings.py

    INSTALLED_APPS += [
        "phonenumber_field",
        "security_txt",
    ]

* Add ``"security_txt"`` to your URLs definitions:

.. code-block:: python

    # urls.py

    from django.urls import re_path


    urlpatterns += [
        re_path(r"^.well-known/security\.txt", include("security_txt.urls")),
    ]

Settings
--------
``SECURITY_TXT_EXPIRES``
    Indicates the date and time after which the data contained in the "security.txt" file is considered stale and should not be used. Defaults to ``None``.
``SECURITY_TXT_PREFERRED_LANGUAGES``
    Used to indicate a set of natural languages that are preferred when submitting security reports. Defaults to ``None``.
``SECURITY_TXT_SIGN``
    Sign "security.txt" using PGP. Defaults to ``False``.
``SECURITY_TXT_SIGNING_KEY``
    Path to PGP key. Defaults to ``""``.

Advanced features
-----------------
If you want to sign your "security.txt":

* Install ``django-security-txt`` with additional dependencies: ``$ pip install django-security-txt[pgp]``.
* Configure:

.. code-block:: python

    # settings.py

    SECURITY_TXT_SIGN = True
    SECURITY_TXT_SIGNING_KEY = "/path/to/key.asc"

Licensing
---------
django-security-txt is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (a
t your option) any later version.
For complete license text see COPYING file.

Contacts
--------
**Project Website**: https://github.com/vint21h/django-security-txt/

**Author**: Alexei Andrushievich <vint21h@vint21h.pp.ua>

For other authors list see AUTHORS file.

.. |GitHub| image:: https://github.com/vint21h/django-security-txt/workflows/build/badge.svg
    :alt: GitHub
.. |Coveralls| image:: https://coveralls.io/repos/github/vint21h/django-security-txt/badge.svg?branch=master
    :alt: Coveralls
.. |pypi-license| image:: https://img.shields.io/pypi/l/django-security-txt
    :alt: License
.. |pypi-version| image:: https://img.shields.io/pypi/v/django-security-txt
    :alt: Version
.. |pypi-django-version| image:: https://img.shields.io/pypi/djversions/django-security-txt
    :alt: Supported Django version
.. |pypi-python-version| image:: https://img.shields.io/pypi/pyversions/django-security-txt
    :alt: Supported Python version
.. |pypi-format| image:: https://img.shields.io/pypi/format/django-security-txt
    :alt: Package format
.. |pypi-wheel| image:: https://img.shields.io/pypi/wheel/django-security-txt
    :alt: Python wheel support
.. |pypi-status| image:: https://img.shields.io/pypi/status/django-security-txt
    :alt: Package status
.. _GitHub: https://github.com/vint21h/django-security-txt/actions/
.. _Coveralls: https://coveralls.io/github/vint21h/django-security-txt?branch=master
.. _pypi-license: https://pypi.org/project/django-security-txt/
.. _pypi-version: https://pypi.org/project/django-security-txt/
.. _pypi-django-version: https://pypi.org/project/django-security-txt/
.. _pypi-python-version: https://pypi.org/project/django-security-txt/
.. _pypi-format: https://pypi.org/project/django-security-txt/
.. _pypi-wheel: https://pypi.org/project/django-security-txt/
.. _pypi-status: https://pypi.org/project/django-security-txt/
