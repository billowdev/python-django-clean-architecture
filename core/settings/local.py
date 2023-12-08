from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p^jj6n*clr_o*(y0ieazv_=%xcj)igx5=0gliiqdyt(pnacz^*'

# # https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR / 'db.sqlite3'),
    },
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'dev_db_name',
    #     'USER': 'dev_db_name',
    #     'PASSWORD': 'test',
    #     'HOST': 'HOST',
    #     'PORT': '5432',
    #     'OPTIONS': {
    #         'sslmode': 'require',
    #         'sslcert': '/certificates/certificate.csr',
    #         'sslkey': '/certificates/certificate.csr',
    #         'sslrootcert': '/certificates/certificate.csr',
    #     }
    # }
}

CSRF_TRUSTED_ORIGINS = []
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = []
CORS_ORIGIN_REGEX_WHITELIST = []