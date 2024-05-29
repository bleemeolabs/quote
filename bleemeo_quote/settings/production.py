from bleemeo_quote.settings.base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ["*"]


DATABASES = {
    "default": {
        "ENGINE": "django_prometheus.db.backends.postgresql",
        "NAME": "bleemeo_quote",
        "USER": "bleemeo_quote_user",
        "PASSWORD": os.environ.get("DJANGO_DATABASE_PASSWORD", "password"),
        "HOST": "postgresql",
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379",
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
        "KEY_PREFIX": "quote",
    }
}

# Fix redis get if cached = 0 or False #115
# CACHES = {
#     "default": {
#         "BACKEND": "django_prometheus.cache.backends.redis.RedisCache",
#         "LOCATION": "redis://redis:6379",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient"
#         },
#         "KEY_PREFIX": "quote"
#     }
# }
