'''Use this for production'''

from .base import *

DEBUG = True
ALLOWED_HOSTS = ['djangodeecooper.herokuapp.com','127.0.0.1']
WSGI_APPLICATION = 'Django_oscar.wsgi.application'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django_oscar.settings.prod")

DATABASES = {
    'default': { 
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd1v49r4m8vrl1t',
        'USER': 'xoosusnhglapwq',
        'PASSWORD': '849fa5ce3949744375b9fbb1f7b36f952ce27a0a3ef1e09db34138d7359a7c5a', 
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

django_heroku.settings(locals())