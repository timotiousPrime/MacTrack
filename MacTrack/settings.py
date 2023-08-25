import os
import django_heroku
import dj_database_url
import secrets

from pathlib import Path

from decouple import Config, Csv
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

config = Config(os.path.join(BASE_DIR, '.env'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY',
                            default=secrets.token_urlsafe(nbytes=64),)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['https://evening-shore-46569-0cd8556ecf85.herokuapp.com/',
                 '127.0.0.1']


CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'members',
    'timesheets',
    'reports',
    'projects',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'MacTrack.urls'

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

WSGI_APPLICATION = 'MacTrack.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)

DATABASES = {
    "default": dj_database_url.config(
        default=config('DATABASE_URL', default='postgres://postgres:password@localhost:5432/MacTrack'),
        conn_max_age=600,
        ssl_require=True,
    )
}

# DATABASES = {
#     "default": dj_database_url.config(
#         default=os.environ.get('DATABASE_URL', 'postgres://postgres:password@localhost:5432/MacTrack'),
#         conn_max_age=600,
#         ssl_require=True
#     )
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "MacTrack",
#         "USER": "postgres",
#         "PASSWORD": 'password',
#         "HOST": "localhost",
#         "PORT": "5432",
#     }
# }

'postgres://postgres:password@localhost:5432/MacTrack'


# DATABASES['default'].update(db_from_env)

# DATABASES = {
#         "default": dj_database_url.config(
#             conn_max_age=600,
#             conn_health_checks=True,
#             ssl_require=True,
#         ),
#     }


# postgres://wtasobjxdyhorf:dd0312fd5b90ba61ddf6dc4ea120dbc8857c5cd96d43c3f767fbd630bedddb7c@ec2-44-215-1-253.compute-1.amazonaws.com:5432/d3f1bhroonsuu4


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Johannesburg'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


django_heroku.settings(locals())

LOGIN_URL = '/login/'