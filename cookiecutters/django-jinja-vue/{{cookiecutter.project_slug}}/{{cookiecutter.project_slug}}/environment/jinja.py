from functools import partial
from decimal import Decimal

from django.contrib import messages
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse

from jinja2 import Environment


def build(**options):
    env = Environment(lstrip_blocks=True, trim_blocks=True, **options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'get_messages': messages.get_messages,
        'DEFAULT_MESSAGE_LEVELS': messages.constants.DEFAULT_LEVELS,
        'zip': zip,
        'list': list
    })
    return env
