from .base import *

DEBUG = True
EMAIL_HOST = "smtp.sohu.com"
EMAIL_HOST_USER = "fgl1989624@sohu.com"
EMAIL_HOST_PASSWORD = "R7YZULV98Q16"
EMAIL_USER_TLS = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
