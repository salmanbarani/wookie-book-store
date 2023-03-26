import decimal

from django.core import validators
from django.db import models


class PositiveDecimalField(models.DecimalField):
    default_validators = [
        validators.MinValueValidator(decimal.Decimal(0)),
    ]

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("max_digits", 8)
        kwargs.setdefault("decimal_places", 2)
        super().__init__(*args, **kwargs)
