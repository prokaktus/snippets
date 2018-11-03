"""
WSGI config for {{cookiecutter.project_name}} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
from os.path import dirname

from django.core.wsgi import get_wsgi_application

from dotenv import load_dotenv


dotenv_path = os.path.join(dirname(dirname(os.path.abspath(__file__))), '.env')
load_dotenv(dotenv_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{cookiecutter.project_slug}}.settings.base")

application = get_wsgi_application()
