"""
Django settings for a_core project.

Generated by 'django-admin startproject' using Django 3.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# for 외부 디비 연결
import dj_database_url  

# for environment
from environ import Env
env = Env()
Env.read_env()
ENVIRONMENT = env('ENVIRONMENT', default='production')

# Feature Toggle
DEVELOPER = env('DEVELOPER', default='')
STAGING = env('STAGING', default=False)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-9lrlv6xa#v850ysn^t2x%5ac@ss_nhhu2(%6&x=!kqcs=p60#o'
SECRET_KEY = env('SECRET_KEY')

# ENCRYPT_KEY = b'5iywR4Xt-JgOzWTA3gMRHiykm3RbRn3mjDVKHA9dvA0='
ENCRYPT_KEY = env('ENCRYPT_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# for environment
if ENVIRONMENT == 'production':
    DEBUG = True
else:
    DEBUG = False

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ["*"]
# ALLOWED_HOSTS = ['localhost', '127.0.0.1', env("RENDER_EXTERNAL_HOSTNAME"),
#                  'www.ttugttag.sbs','ttugttag.sbs',]
# ALLOWED_HOSTS = ['localhost', '127.0.0.1',
#                  'www.ttugttag.sbs','ttugttag.sbs',]
# CSRF_TRUSTED_ORIGINS =[ 'https://*.onrender.com',
#                         'https://*.ttugttag.sbs/', 'https://ttugttag.sbs/',]

# ALLOWED_HOSTS = ['localhost', '127.0.0.1','huttag.up.railway.app']
# CSRF_TRUSTED_ORIGINS =['https://huttag.up.railway.app/']

# CSRF_TRUSTED_ORIGINS = [ 'huttag.up.railway.app' ]
# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# CSRF_COOKIE_SECURE = True

INTERNAL_IPS = (
    '127.0.0.1',
    'localhost:8000'
)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # for allauth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    # for cloudinary
    'cloudinary_storage',
    'cloudinary',
    # Optional -- requires install using `django-allauth[socialaccount]`.
    'allauth.socialaccount',
    # for honeypot
    "admin_honeypot",
    # for cleanup
    'django_cleanup.apps.CleanupConfig',
    # for sitemaps
    'django.contrib.sitemaps',    
    # for django_htmx
    'django_htmx',
    # for app    
    'a_posts',
    'a_users',
    'a_features',
    'a_landingpages',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # for allauth:
    'allauth.account.middleware.AccountMiddleware',
    # for django_htmx
    'django_htmx.middleware.HtmxMiddleware',
    # for whitenoise
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # for a_landingpages    
    'a_landingpages.middleware.landingpage_middleware',    
]

ROOT_URLCONF = 'a_core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request', # fro allouth 이미 정의 됌
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'a_core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# for 외부 디비 연결
POSTGRES_LOCALLY = False    # or  False      <===== True 면 postgres   False면 local sqlite3
if ENVIRONMENT == 'production' or POSTGRES_LOCALLY == True:
    DATABASES['default'] = dj_database_url.parse(env("DATABASE_URL"))

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

# USE_TZ = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[BASE_DIR / 'static']
# for whitenoise for collectstatic
STATIC_ROOT=BASE_DIR / 'staticfiles'

MEDIA_URL = 'media/'

# for media server
if ENVIRONMENT == "production" or POSTGRES_LOCALLY == True:
    # DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    STORAGES = {
        "default": {
            "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
            },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
            },
    }

    # for cloudinary
    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': env('CLOUD_NAME'),
        'API_KEY': env('CLOUD_API_KEY'),
        'API_SECRET': env('CLOUD_API_SECRET'),    
    }
else:
    MEDIA_ROOT = BASE_DIR / 'media'

# # for cloudinary
# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME': env('CLOUD_NAME'),
#     'API_KEY': env('CLOUD_API_KEY'),
#     'API_SECRET': env('CLOUD_API_SECRET'),    
# }

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = "/"

# for email authentication
if ENVIRONMENT == "production" or POSTGRES_LOCALLY == True:    
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = env('EMAIL_ADDRESS')
    EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    # DEFAULT_FROM_EMAIL = 'Awesome'
    DEFAULT_FROM_EMAIL = f'TTuaTTag {env("EMAIL_ADDRESS")}'
    ACCOUNT_EMAIL_SUBJECT_PREFIX = ''
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True

# ACCOUNT_USERNAME_BLACKLIST = [ 'admin', 'accounts', 'profile', 'category', 'post' ]
ACCOUNT_USERNAME_BLACKLIST = [ 'admin', 'accounts', 'profile', 'category', 'post', 'theboss' ]
# ACCOUNT_USERNAME_BLACKLIST = [ 'admin', 'accounts', 'profile', 'category', 'post', 'inbox', 'theboss' ]
