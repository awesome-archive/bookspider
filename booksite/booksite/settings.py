# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kr71xy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',

    'corsheaders',
    'rest_framework',
    'rest_framework_jwt',
    'djoser',

    'threadedcomments',
    'django_comments',
    'robots',
    'raven.contrib.django.raven_compat',
    'django_assets',
    'captcha',
    'graphene_django',
    'booksite.book',
    'booksite.usercenter',
    'booksite.background',
    'booksite.h5',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'booksite.usercenter.middleware.JWTAuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
)

ROOT_URLCONF = 'booksite.urls'

WSGI_APPLICATION = 'booksite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

GRAPHENE = {
    'SCHEMA': 'booksite.schema.schema'
}

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

SITE_ID = 1

COMMENTS_APP = 'threadedcomments'

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            os.path.join(BASE_DIR, 'booksite/templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
                "booksite.context_processors.analystics",
                "booksite.context_processors.categorys",
                "booksite.context_processors.bookmark_update_count",
            ],
        },
    },
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'booksite/static'),
)
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "django_assets.finders.AssetsFinder"
)
MEDIA_ROOT = os.path.join(BASE_DIR, 'bookstore')
MEDIA_URL = '/media/'

AUTH_USER_MODEL = 'usercenter.User'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': '127.0.0.1:6379:1',
        'KEY_PREFIX': 'booksite',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PASSWORD': '',
        }
    }
}

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '***********@gmail.com'
EMAIL_HOST_PASSWORD = '******'
EMAIL_SUBJECT_PREFIX = u'[kanxiaoshuo.me]'
EMAIL_USE_TLS = True

BROKER_URL = 'amqp://guest:guest@localhost:5672//'

DJOSER = {
    'DOMAIN': os.environ.get('DJANGO_DJOSER_DOMAIN', 'bobdylan.local'),
    'SITE_NAME': os.environ.get('DJANGO_DJOSER_SITE_NAME', 'my site'),
    'PASSWORD_RESET_CONFIRM_URL': '?action=set-new-password&uid={uid}&token={token}',
    'ACTIVATION_URL': '?action=activate&uid={uid}&token={token}',
    'SEND_ACTIVATION_EMAIL': False,
}

JWT_AUTH = {
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),
}

try:
    from .local_settings import *
except:
    raise ImportError('应当使用与settings同级别目录下的local_settings文件')
