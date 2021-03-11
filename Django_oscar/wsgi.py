import os

from django.core.wsgi import get_wsgi_application
# from whitenoise.django import DjangoWhiteNoise
from whitenoise import WhiteNoise


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django_oscar.settings.prod")

application = get_wsgi_application()
application = WhiteNoise(application, root='/static')

# application = DjangoWhiteNoise(application)
