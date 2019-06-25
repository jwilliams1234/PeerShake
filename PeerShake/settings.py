"""
Django settings for PeerShake project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import json

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_URL = os.environ.get('BASE_URL', '')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'cs2-i_zc6mi@n-eg7!*ijlqyv%t8^pefzg@!bw00a43g36!yyy')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = json.loads(os.environ.get('DEBUG', 'false'))

ALLOWED_HOSTS = [
    'localhost',
    'peershake.cloud',
    'amp.pharm.mssm.edu',
    '127.0.0.1',
]

SITE_ID=3

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'livereload',
    'rest_auth',
    'rest_auth.registration',
     # 'extensions.ajax_select_ex',
    'extensions.allauth_ex',
    # 'extensions.drf_yasg_ex',
    'extensions.rest_auth_ex',
    'extensions.rest_framework_ex',
    # 'django_extensions',
    # 'django_extensions',
    'bootstrapform',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.orcid',
    'allauth.socialaccount.providers.globus',
    # 'rest_framework',
    # 'rest_framework.authtoken',
    'django.contrib.staticfiles',
    'PeerShakeWeb',
    'crispy_forms',
    'sslserver',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 
CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # TODO: fix pagination handling so these values can be different
    'PAGE_SIZE': 11,
    'VIEW_PAGE_SIZE': 11,
    'SEARCH_PAGE_SIZE': 11,
    'EXCEPTION_HANDLER': 'extensions.rest_framework_ex.exeptions.handler',
    'URL_FIELD_NAME': 'get_url',
}

ROOT_URLCONF = 'PeerShake.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'PeerShakeWeb', 'templates',),
            os.path.join(BASE_DIR, 'extensions', 'allauth_ex', 'templates',),
            os.path.join(BASE_DIR, 'extensions', 'ajax_select_ex', 'templates',),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'django.contrib.template.context_processors.request',
            ],
            'builtins': [
                'django.contrib.staticfiles.templatetags.staticfiles',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

WSGI_APPLICATION = 'PeerShake.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': json.loads(os.environ.get('DATABASE_CONFIG', json.dumps({
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    })))
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/' + BASE_URL + 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

LOGIN_URL = '/' + BASE_URL + 'accounts/login/'
LOGOUT_URL = '/' + BASE_URL + 'accounts/logout/'

LOGIN_REDIRECT_URL = '/' + BASE_URL
LOGOUT_REDIRECT_URL = '/' + BASE_URL

ACCOUNT_LOGIN_REDIRECT_URL = LOGIN_REDIRECT_URL
ACCOUNT_LOGOUT_REDIRECT_URL = LOGOUT_REDIRECT_URL
