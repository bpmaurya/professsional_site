'''Use this for development '''

from .base import *
ALLOWED_HOSTS += ['127.0.0.1']
DEBUG = True

WSGI_APPLICATION = 'Django_oscar.wsgi.application'
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django_oscar.settings.dev")


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
        'PASSWORD': '849fa5ce3949744375b9fbb1f7b36f952ce27a0a3ef1e09db34138d7359a7c5a', 
        'HOST': 'ec2-54-161-239-198.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

# CORS_ORIGIN_WHITELIST = ('http://localhost:8000', )