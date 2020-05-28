from .base import *

DEBUG = False
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'AOKops',
        'USER': 'admin',
        'PASSWORD': 'mysqlpass',
        'HOST': '127.0.0.1',
        'PORT': '',
        'OPTIONS': {},
        'init_command': 'set storage_engine=INNODB,'
                        'SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED, autocommit=1, names "utf8";'
    }
}
