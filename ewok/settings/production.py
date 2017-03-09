# Fetch our common settings
import os
from common import *

# #########################################################

# ##### DEBUG CONFIGURATION ###############################
DEBUG = True
LOGIN_REDIRECT_URL = '/myaccount/' 

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
    '95.213.200.78',
    '127.0.0.1',
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


NODE_EXEC = os.popen("which %s" % "nodejs").read().strip()
if not NODE_EXEC:
    NODE_EXEC = os.popen("which %s" % "node").read().strip()
