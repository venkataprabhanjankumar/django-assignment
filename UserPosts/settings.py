from pathlib import Path
from decouple import config, Csv
import os
import string

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY', default=string.ascii_letters)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1', cast=Csv())


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'crispy_forms',

    'users.apps.UsersConfig',
    'products.apps.ProductsConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'UserPosts.urls'

AUTH_USER_MODEL = 'users.UserModel'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'UserPosts.wsgi.application'


DATABASES = {
    'default': {},
    'UsersDb': {
        'ENGINE': 'django.db.backends.mysql',
        'USER': config('USERDB_USER'),
        'PASSWORD': config('USERDB_PASSWORD'),
        'NAME': config('USERDB_NAME'),
        'HOST': config('USERDB_HOST'),
    },
    'ProductsDb': {
        'ENGINE': 'django.db.backends.postgresql',
        'USER': config('PRODUCTSDB_USER'),
        'PASSWORD': config('PRODUCTSDB_PASSWORD'),
        'NAME': config('PRODUCTSDB_NAME'),
        'HOST': config('PRODUCTSDB_HOST'),
    }
}

DATABASE_ROUTERS = [
    'routers.ModelRoutes.UsersModel',
    'routers.ModelRoutes.ProductsModel'
]


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
