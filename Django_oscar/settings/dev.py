'''Use this for development '''

from .base import *
ALLOWED_HOSTS += ['127.0.0.1']
DEBUG = False

WSGI_APPLICATION = 'Django_oscar.wsgi.dev.application'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django_oscar.settings.dev")


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

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

# CORS_ORIGIN_WHITELIST = ('http://localhost:8000', )