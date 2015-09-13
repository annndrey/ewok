# Fetch our common settings
from common import *

# #########################################################

# ##### DEBUG CONFIGURATION ###############################
DEBUG = False


# ##### DATABASE CONFIGURATION ############################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'exam',
        'USER': 'exam',
        'PASSWORD': 'exam',
        'HOST': '127.0.0.1',
    }
}

# ##### APPLICATION CONFIGURATION #########################

INSTALLED_APPS = DEFAULT_APPS

NODE_EXEC = 'nodejs'
ALLOWED_HOSTS = [
    'test.psy-point.ru',
    'psy-point.ru',
    '95.213.200.78'
]


CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': 'localhost:6379',
        'OPTIONS': {
            'DB': 2,
        },
    },
}
