
from project1 import settings_extra
SECRET_KEY = settings_extra.SECRET_KEY
ALLOWED_HOSTS = settings_extra.ALLOWED_HOSTS
DEBUG = settings_extra.DEBUG
IS_CLUB = settings_extra.IS_CLUB
TITLE = settings_extra.TITLE

TEMPLATE_DEBUG = DEBUG
'''
DEBUG = True
SECRET_KEY = 'x'
IS_CLUB = True
TITLE= 'TEMPORARY HEADING'
ALLOWED_HOSTS = ['.cliveogilvie.pythonanywhere.com',]
'''
"""
For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mysite',
    'events',
    'users',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-uk'


DATE_INPUT_FORMATS = (
    '%Y-%m-%d',              # '2006-10-25'
    '%d/%m/%Y',              # '25/10/2006'
    '%d/%m/%y',              # '25/10/06'
)

'''
DATE_INPUT_FORMATS = (
    '%d%m%y',              # '251006'
    '%d/%m/%y',              # '25/10/06'
    '%Y-%m-%d',              # '2006-10-25'
    '%d/%m/%Y',              # '25/10/2006'
)
'''

DATE_FORMAT = "l jS F Y"
TIME_ZONE = 'Europe/London'
LOGIN_REDIRECT_URL = '/'
USE_I18N = True
USE_L10N = False
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#STATICFILES_DIRS = os.path.join(BASE_DIR, 'static')
