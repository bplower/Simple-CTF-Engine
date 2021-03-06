"""
Django settings for SimpleCTFEngine project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
import secretConfigs
import ldap
from django_auth_ldap.config import LDAPSearch
from django_auth_ldap.config import NestedActiveDirectoryGroupType

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secretConfigs.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# LDAP Settings
# http://pythonhosted.org/django-auth-ldap/example.html
# http://www.spannerbracket.com/wordpress/?p=40

# Binding and connection options
#AUTH_LDAP_START_TLS = True # If you've enabled TLS on your active directory server, uncomment this line
AUTH_LDAP_SERVER_URI = secretConfigs.AUTH_LDAP_SERVER_URI
AUTH_LDAP_BIND_DN = secretConfigs.AUTH_LDAP_BIND_DN
AUTH_LDAP_BIND_PASSWORD = secretConfigs.AUTH_LDAP_BIND_PASSWORD
AUTH_LDAP_CONNECTION_OPTIONS = {
	ldap.OPT_DEBUG_LEVEL: 1,
	ldap.OPT_REFERRALS: 0,
}

# User and group search objects and types
AUTH_LDAP_USER_SEARCH = LDAPSearch(secretConfigs.LDAP_USER_SEARCH_BASE, ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)")
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(secretConfigs.LDAP_GROUP_SEARCH_BASE, ldap.SCOPE_SUBTREE, "(objectClass=group)")
AUTH_LDAP_GROUP_TYPE = NestedActiveDirectoryGroupType()

# Cache settings
AUTH_LDAP_CACHE_GROUPS = True
AUTH_LDAP_GROUP_CACHE_TIMEOUT = 300

# What to do once the user is authenticated
AUTH_LDAP_USER_ATTR_MAP = {
	"first_name": "givenName",
	"last_name": "sn",
	"email": "mail"
}
# AUTH_LDAP_USER_FLAGS_BY_GROUP = {
# 	"is_staff": ["CN=ESXI Administrators,OU=Groups,OU=CSC,DC=csc,DC=uaf,DC=edu"]
# }
# AUTH_LDAP_FIND_GROUP_PERMS = True

# The backends needed to make this work.
AUTHENTICATION_BACKENDS = (
	'django_auth_ldap.backend.LDAPBackend',
	'django.contrib.auth.backends.ModelBackend'
)

# Application definition
INSTALLED_APPS = (
	'SimpleCTFEngine',
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'SimpleCTFEngine.urls'

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

WSGI_APPLICATION = 'SimpleCTFEngine.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_ROOT = ''
STATICFILES_DIRS = (BASE_DIR + '/static/',)
STATIC_URL = '/static/'

# Logging Settings
LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'handlers': {
		'mail_admins': {
			'level': 'ERROR',
			'class': 'django.utils.log.AdminEmailHandler'
		},
		'stream_to_console': {
			'level': 'DEBUG',
			'class': 'logging.StreamHandler'
		},
	},
	'loggers': {
		'django.request': {
			'handlers': ['mail_admins'],
			'level': 'ERROR',
			'propagate': True,
		},
		'django_auth_ldap': {
			'handlers': ['stream_to_console'],
			'level': 'DEBUG',
			'propagate': True,
		},
	}
}