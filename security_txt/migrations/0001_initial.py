# -*- coding: utf-8 -*-

# django-security-txt
# security_txt/migrations/0001_initial.py

# Generated by Django 3.1.7 on 2021-03-21 08:52


from typing import List, Tuple

from django.db import models, migrations
from django.core.validators import URLValidator
from django.db.migrations.operations.base import Operation


__all__: List[str] = ["Migration"]


class Migration(migrations.Migration):
    """Migration."""

    initial: bool = True

    dependencies: List[Tuple[str, str]] = []

    operations: List[Operation] = [
        migrations.CreateModel(
            name="Acknowledgment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "url",
                    models.URLField(
                        db_index=True,
                        max_length=512,
                        unique=True,
                        validators=[URLValidator(schemes=["https"])],
                        verbose_name="link to page where security researchers are recognized",  # noqa: E501
                    ),
                ),
            ],
            options={
                "verbose_name": "acknowledgment",
                "verbose_name_plural": "acknowledgments",
                "ordering": ["url"],
            },
        ),
    ]
