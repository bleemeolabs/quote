from bleemeo_quote.settings.base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bleemeo_quote',
        'USER': 'bleemeo_quote_user',
        'PASSWORD': os.environ.get("DJANGO_DATABASE_PASSWORD", 'password'),
        'HOST': 'mysql',
    }
}
