"""
Django settings for VanEsthetique project production.

"""
from .base import *

SECRET_KEY = 'q1eXSi5`IVn\\drJr[\x0c)5{xc!'

DEBUG = False

ALLOWED_HOSTS = ['vanesthetique.herokuapp.com', '127.0.0.1']

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # on utilise l'adaptateur postgresql
            'NAME': 'BD_VanEsthetique', # le nom de notre base de donnees creee precedemment
            'USER': 'Angel', # attention : remplacez par votre nom d'utilisateur
            'PASSWORD': 'angel',
            'HOST': '',
            'PORT': '5432',
    }
}
# MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

# Static files settings
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)
# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)