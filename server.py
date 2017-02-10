'''
Run this with `$ python ./mini_django.py runserver` and go
to http://localhost:8000/
'''
import os
import sys
from django.conf import settings


# this module
me = os.path.splitext(os.path.split(__file__)[1])[0]
# helper function to locate this dir
here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)

# SETTINGS
DEBUG = True
ROOT_URLCONF = me
DATABASES = {'default': {}}  # required regardless of actual usage
TEMPLATE_DIRS = (
    here('.'),  # Templates in current dir
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATE_DIRS,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': (
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
            ),
        },
    },
]
SECRET_KEY = 'so so secret'
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
)
INSTALLED_APPS = (
    'django.contrib.sessions',
)
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    here('static'),
)

SILENCED_SYSTEM_CHECKS = ['1_8.W001']  # Silance warning for using TEMPLATE_*

if not settings.configured:
    settings.configure(**locals())

from django.shortcuts import render
# Settings must be configured before importing some things
# from django.views.decorators.csrf import csrf_exempt


# VIEW
def index(request, name=None):
    return render(request, 'index.html', {'name': name})


# URLS
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', index),
    url(r'^(?P<name>\w+)?$', index),
]

urlpatterns += staticfiles_urlpatterns()

if __name__ == '__main__':
    # set the ENV
    sys.path += (here('.'),)
    # run the development server
    from django.core import management
    management.execute_from_command_line()
