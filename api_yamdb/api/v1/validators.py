import re

from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


@deconstructible
class ASCIIUsernameValidator(validators.RegexValidator):
    regex = r"^[\w.@+-]+\Z"
    message = _(
        "Enter a valid username. This value may contain only ASCII letters, "
        "numbers, and @/./+/-/_ characters."
    )
    flags = re.ASCII


@deconstructible
class UnicodeUsernameValidator(validators.RegexValidator):
    regex = r"^[\w.@+-]+\Z"
    message = _(
        "Enter a valid username. This value may contain only letters, "
        "numbers, and @/./+/-/_ characters."
    )
    flags = 0


def username(value):
    if value == 'me':
        raise serializers.ValidationError('Недопустимое имя пользователя')
    return value
