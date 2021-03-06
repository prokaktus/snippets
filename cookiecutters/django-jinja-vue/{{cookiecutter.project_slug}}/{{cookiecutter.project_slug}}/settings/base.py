"""
Django settings for {{cookiecutter.project_slug}} project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

import raven

from ._utils import getenv


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv('SECRET_KEY', 'Not Secure Default s3cRE+t')

# SECURITY WARNING: don't run with debug turned on in production!
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getenv('DEBUG', False)

ALLOWED_HOSTS = getenv('ALLOWED_HOSTS', 'localhost').split(',')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'apps.base',
    'apps.users'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = '{{cookiecutter.project_slug}}.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'APP_DIRS': True,
        'OPTIONS': {
            'extensions': [],
            'environment': '{{cookiecutter.project_slug}}.environment.jinja.build',
            'context_processors': []
        },
        'DIRS': [
            os.path.join(BASE_DIR, '{{cookiecutter.project_slug}}', 'jinja2'),
        ],
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = '{{cookiecutter.project_slug}}.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', '{{cookiecutter.project_slug}}'),
        'USER': os.getenv('DB_USER', '{{cookiecutter.project_slug}}'),
        'PASSWORD': os.getenv('DB_PASSWORD', '{{cookiecutter.project_slug}}'),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# AUTH strategies
AUTH_USER_MODEL = 'users.User'


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'


# analytics / tracking section
GOOGLE_ANALYTICS = getenv('GOOGLE_ANALYTICS', '')
YANDEX_METRICA = getenv('YANDEX_METRICA', '')
TOP_MAILRU = getenv('TOP_MAILRU', '')


# Sentry settings
if not DEBUG:
    RAVEN_CONFIG = {
        'dsn': getenv('SENTRY_DSN'),
        # If you are using git, you can also automatically configure the
        # release based on the git info.
        'release': raven.fetch_git_sha(BASE_DIR),
    }
    RAVENJS_CONFIG = os.getenv('SENTRY_DSN_JS', '')
else:
    RAVENJS_CONFIG = ''


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_STORAGE = '{{ cookiecutter.project_slug }}.storage.FileStorage'


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Logging configuration

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(pathname)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'echo': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        } if getenv('LOGGING_ENABLE_ECHO', False) else {'class': 'logging.NullHandler'},
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '/var/log/{{cookiecutter.project_slug}}/django.log',
            'formatter': 'verbose',
            'when': 'D'
        } if enable_file_logging else {'class': 'logging.NullHandler'}
    },
    'loggers': {
        'django': {
            'handlers': ['echo', 'file'],
            'level': getenv('LOGGING_LEVEL_DJANGO', 'INFO'),
            'propagate': True,
        },
        'django.db': {
            'handlers': ['echo', 'file'],
            'level': getenv('LOGGING_LEVEL_DJANGO_DB', 'INFO'),
            'propagate': False
        },
        'apps': {
            'handlers': ['file', 'echo'],
            'level': getenv('LOGGING_LEVEL_MAIN', 'INFO'),
            'propagate': False
        },
        '{{cookiecutter.project_slug}}': {
            'handlers': ['file', 'echo'],
            'level': getenv('LOGGING_LEVEL_MAIN', 'INFO'),
            'propagate': False
        },
    },
}
