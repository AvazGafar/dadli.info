"""
Django settings for dadli project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w!@*zud_lf!^w!8kgbq*4twq=urrydsast9b(c)a4s-nakj65o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'materializecssform',
    'pers',
    'comp1',
	'social_django',
	'authent',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware', #for multi-language
	'social_django.middleware.SocialAuthExceptionMiddleware', 
]

#for multi-language
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale/'), 
	os.path.join(BASE_DIR, 'pers/locale/'),
	os.path.join(BASE_DIR, 'authent/locale/'),
	os.path.join(BASE_DIR, 'comp1/locale/'),
	
]


ROOT_URLCONF = 'dadli.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
				'django.template.context_processors.i18n', #for multi-language
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
				'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect'
            ],
        },
    },
]

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.debug.debug',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'social.pipeline.debug.debug',
)
WSGI_APPLICATION = 'dadli.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dadli.info',
		'USER': 'dadliuser',
		'PASSWORD': 'dartika456987',
		'HOST': 'localhost',
		'PORT': '3306',
		
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = [
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
	'social_core.backends.linkedin.LinkedinOAuth2',
	'social_core.backends.google.GoogleOAuth2',

    'django.contrib.auth.backends.ModelBackend',
]

SOCIAL_AUTH_GOOGLE_OAUTH2_IGNORE_DEFAULT_SCOPE = True
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
'https://www.googleapis.com/auth/userinfo.email',
'https://www.googleapis.com/auth/userinfo.profile'
]

# Google+ SignIn (google-plus)
SOCIAL_AUTH_GOOGLE_PLUS_IGNORE_DEFAULT_SCOPE = True
SOCIAL_AUTH_GOOGLE_PLUS_SCOPE = [
'https://www.googleapis.com/auth/plus.login',
'https://www.googleapis.com/auth/userinfo.email',
'https://www.googleapis.com/auth/userinfo.profile'
]
SOCIAL_AUTH_GOOGLE_OAUTH2_USE_DEPRECATED_API = True
SOCIAL_AUTH_GOOGLE_PLUS_USE_DEPRECATED_API = True
LOGIN_URL = '/login/'
# GOOGLE+ login
LOGIN_REDIRECT_URL = 'http://127.0.0.1:8000/oauth/complete/google-oauth2/'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '853172642986-cnt921hhl62kthdgtnp8e8rou0231mkg.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '4UcGgq16ZJ6YNFYSAKwONJOG'





# FACEBOOK login

SOCIAL_AUTH_FACEBOOK_KEY = '437772979967237'
SOCIAL_AUTH_FACEBOOK_SECRET = '718d26af943e3ba26a20577096168dc2'

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'locale': 'az_AZ',
  'fields': 'id, name, email, age_range'
}

LOGIN_REDIRECT_URL = 'http://127.0.0.1:8000/oauth/complete/facebook-oauth2/'

SOCIAL_AUTH_LOGIN_ERROR_URL = '/settings/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/settings/'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False

#Linkedin
SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '865n2mv0yv8okh'
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = 'Cmmnk4kpFRNDiJeR'

#twitter
SOCIAL_AUTH_TWITTER_KEY = 'gItFgWrtA40y9CSSjXembzc8K'
SOCIAL_AUTH_TWITTER_SECRET = 'oCZieUzASxVprCVI9uFYJTGjAbSiz7lPzQ9MQAHAPOXmVw7Z1y'
from dadli.config import *

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/members/'
LOGIN_ERROR_URL = '/login-error/'

SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'
SOCIAL_AUTH_UID_LENGTH = 16
SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 16
SOCIAL_AUTH_NONCE_SERVER_URL_LENGTH = 16
SOCIAL_AUTH_ASSOCIATION_SERVER_URL_LENGTH = 16
SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 16
SOCIAL_AUTH_ENABLED_BACKENDS = ('twitter',)




# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'az'

TIME_ZONE = 'UTC'

#for multi-language
USE_I18N = True

USE_L10N = True

USE_TZ = True

#for multi-language
ugettext = lambda s: s
LANGUAGES = (
    ('az', ugettext('Azərbaycan dili')),
    ('en', ugettext('English')),
	('ru', ugettext('Русский')),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
