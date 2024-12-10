"""
Django settings for bloomerz project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
<<<<<<< HEAD

from pathlib import Path
=======
from __future__ import absolute_import, unicode_literals
from pathlib import Path
from dotenv import load_dotenv


import os

import dj_database_url

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bloomerz.settings')


>>>>>>> 1f361375759c1105842deef4a7c9c88b7b8e1a9f

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
<<<<<<< HEAD
SECRET_KEY = 'django-insecure-f32^^)ubxvcaiaqtyk5))^ndjug!smw=+3z*tu5rzlkh#^mqan'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
=======
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
if not 'ON_HEROKU' in os.environ:
    DEBUG = True


ALLOWED_HOSTS = ["*"]
>>>>>>> 1f361375759c1105842deef4a7c9c88b7b8e1a9f


# Application definition

INSTALLED_APPS = [
<<<<<<< HEAD
    'django_browser_reload',
    'theme',
    'tailwind',
=======
    # 'django_browser_reload',
    
    'django_crontab',
    'theme',
    'tailwind',
    
>>>>>>> 1f361375759c1105842deef4a7c9c88b7b8e1a9f
    'main_app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
<<<<<<< HEAD
]

MIDDLEWARE = [
    'django_browser_reload.middleware.BrowserReloadMiddleware',
    'django.middleware.security.SecurityMiddleware',
=======
    'celery',
    'django_celery_beat',
    
]

MIDDLEWARE = [
    # 'django_browser_reload.middleware.BrowserReloadMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
>>>>>>> 1f361375759c1105842deef4a7c9c88b7b8e1a9f
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bloomerz.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'bloomerz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
<<<<<<< HEAD

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bloomerz',
    }
}
=======
if 'ON_HEROKU' in os.environ:
    DATABASES = {
        'default': dj_database_url.config(
            env='DATABASE_URL',
            conn_max_age=600, 
            conn_health_checks=True,
            ssl_require=True)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'bloomerz',
        }
    }
>>>>>>> 1f361375759c1105842deef4a7c9c88b7b8e1a9f



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

<<<<<<< HEAD
STATIC_URL = 'static/'
LOGIN_URL = ''
=======
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"
LOGIN_URL = 'login'
>>>>>>> 1f361375759c1105842deef4a7c9c88b7b8e1a9f
LOGIN_REDIRECT_URL = 'garden-index'
LOGOUT_REDIRECT_URL = 'home'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INTERNAL_IPS = [
    "127.0.0.1",
]

TAILWIND_APP_NAME = 'theme'

<<<<<<< HEAD
=======

CRONJOBS = [
    ('0 * * * *', 'main_app.cron.update_date')
]

CELERY_BROKER_URL = os.getenv('REDIS_URL')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
>>>>>>> 1f361375759c1105842deef4a7c9c88b7b8e1a9f
