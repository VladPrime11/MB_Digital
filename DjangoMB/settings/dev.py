from .base import *
from decouple import config

DEBUG = config('DEBUG', default=True, cast=bool)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
SECRET_KEY = config('SECRET_KEY')
