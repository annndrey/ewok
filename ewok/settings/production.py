# Import some utility functions
from os.path import join
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