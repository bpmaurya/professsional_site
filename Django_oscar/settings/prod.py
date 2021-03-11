'''Use this for production'''

from .base import *

DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1','djangodeecooper.herokuapp.com']
WSGI_APPLICATION = 'Django_oscar.wsgi.prod.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd1v49r4m8vrl1t',
        'USER': 'xoosusnhglapwq',
        'PASSWORD': 'db_password', 
        'HOST': 'ec2-54-161-239-198.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
