"""
Django settings for NewsPaper2 project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-t5w1)7lgpw6ko&zsff)b9ar&5dz*82u@qj1op+%d#0p$%mtkdd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"

# APSCHEDULER_RUN_NOW_TIMEOUT = 25

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'news3.apps.News3Config',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    'django.contrib.sites',
    'django.contrib.flatpages',

    'django_filters',
    'django_apscheduler',

]



MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]



ROOT_URLCONF = 'NewsPaper3.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request'
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',

    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'NewsPaper3.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SITE_ID = 1

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

LOGIN_URL = 'sign/login/'
LOGIN_REDIRECT_URL = '/'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = "mandatory"

ACCOUNT_FORMS = {'sign': 'sign.models.BasicSignupForm'}

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_SSL = True


DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[{asctime}] [{levelname}] {message}',
            'style': '{',
        },
        'warning_format': {
            'format': '[{asctime}] [{levelname}] {message} {pathname}',
            'style': '{',
        },
        'error_format': {
            'format': '[{asctime}] [{levelname}] {message} {pathname} {exc_info}',
            'style': '{',
        },
        'info_file_format': {
            'format': '[{asctime}] [{levelname}] {module} {message}',
            'style': '{',
        },
        'error_file_format': {
            'format': '[{asctime}] * [{levelname}] {message} {pathname} {exc_info}',
            'style': '{',
        },
        'error_mail_format': {
            'format': '[{asctime}] [{levelname}] {message} {pathname}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console': {
            # 'level': 'DEBUG',
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'NewsPaper3.custom_logger.CustomHandler',
            # 'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'warning_format'
        },
        'console_error': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'error_format'
        },
        'general_log': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'info_file_format'
        },
        'error_log': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
            'formatter': 'error_file_format'
        },
        'security_log': {
            'class': 'logging.FileHandler',
            'filename': 'security.log',
            'formatter': 'info_file_format'
        },
        'mail_admins': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'error_mail_format',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['general_log', 'console_error', 'console_warning',  'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['error_log', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.server': {
            'handlers': ['error_log', 'mail_admins' ],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.template': {
            'handlers': ['error_log'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db_backends': {
            'handlers': ['error_log'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['security_log'],
            'propagate': True,
        },
    }
}

ADMINS = [("admin", "admin@example.com")]