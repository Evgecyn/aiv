# -*- coding: utf-8 -*-

import os

gettext_noop = lambda s: s

ADMINS = (
    ('a-iv', 'alexander.vl.ivanov@gmail.com'),
)

MANAGERS = ADMINS

EMAIL_SUBJECT_PREFIX = '[aiv]'

DATABASE_ENGINE = 'postgresql_psycopg2'    # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'aiv'
DATABASE_USER = 'aiv'             # Not used with sqlite3.
DATABASE_PASSWORD = 'password'         # Not used with sqlite3.
DATABASE_HOST = 'localhost'             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = '5432'             # Set to empty string for default. Not used with sqlite3.

TIME_ZONE = 'Asia/Yekaterinburg'

LANGUAGE_CODE = 'ru'

SITE_ID = 1

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin_media/'

# Don't share this with anybody.
SECRET_KEY = '6^nwy#-yrjdxe^3&#hkc-rg4jyw*r85wtcpm0wpgv0y_#7s843'

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.multilingual.MultilingualURLMiddleware',
]

ROOT_URLCONF = 'aiv.urls'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'config',
    'cms',
    'cms.plugins.text',
    'cms.plugins.picture',
    'cms.plugins.link',
    'cms.plugins.file',
    'cms.plugins.snippet',
    'cms.plugins.googlemap',
    'mptt',
    'publisher',
    'reversion',
    'south',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates'),
)

FIXTURE_DIRS = (
    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'fixtures'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'cms.context_processors.media',
)

# Server settings
FORCE_SCRIPT_NAME = ''

CACHE_BACKEND = 'locmem:///?max_entries=5000'

# django-config settings
CONFIG_SITES = ['www.a-iv.info', ]
CONFIG_REDIRECTS = ['a-iv.info', ]

# django-cms
CMS_TEMPLATES = (
        ('base.html', gettext_noop('default')),
        ('frontpage.html', gettext_noop('front page')),
)

LANGUAGES = (
        ('ru', gettext_noop('Russian')),
        ('en', gettext_noop('English')),
)
