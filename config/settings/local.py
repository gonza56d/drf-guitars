from os import environ

from .base import *


DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': environ.get('POSTGRES_DB'),
        'USER': environ.get('POSTGRES_USERNAME'),
        'PASSWORD': environ.get('POSTGRES_PASSWORD'),
        'HOST': environ.get('POSTGRES_HOST'),
        'PORT': environ.get('POSTGRES_PORT'),
    }
}
