import os

import dj_database_url

from .settings import *  # noqa


DEBUG = str(os.environ.get('DEBUG', 'false')).lower() == 'true'

DATABASES = {'default': dj_database_url.config()}
