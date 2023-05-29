from pathlib import Path

import environ


environ.Env.read_env(Path(__file__).resolve().parent.parent / '.env')

env = environ.Env(
    DEBUG=(bool),
    SECRET_KEY=(str),
    DATABASES_NAME=(str),
    DATABASES_USER=(str),
    DATABASES_PASSWORD=(str),
    DATABASES_HOST=(str),
    DATABASES_PORT=(int),
    DJANGO_SUPERUSER_USERNAME=(str),
    DJANGO_SUPERUSER_EMAIL=(str),
    DJANGO_SUPERUSER_PASSWORD=(str),
    DOMAIN_NAME=(str),
)
