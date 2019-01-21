"""
Django settings for VanEsthetique project développement.

"""
from .base import *

SECRET_KEY = 'sgzfpvfiy)eb8&32w@_jt6w4#9w^%#m3jdn9cs4)bj(_%qh+%r'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

INSTALLED_APPS += ['debug_toolbar']

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
INTERNAL_IPS = ['127.0.0.1', '::1']