import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)
TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')
TEMPLATE_PATH_PROTO = os.path.join(TEMPLATE_PATH, 'proto')
TEMPLATE_PATH_PROTO_COMMON = os.path.join(TEMPLATE_PATH_PROTO, 'common')
SITE_ID = 1
SERVER_EMAIL = 'gofisher.shop@gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'gofisher.shop@gmail.com'
EMAIL_HOST_PASSWORD = '12345tratata'
EMAIL_PORT =587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'gofisher.shop@gmail.com'
CCOUNT_ACTIVATION_DAYS='2'

DEBUG = True

ALLOWED_HOSTS = ['46.101.144.152', 'localhost', '127.0.0.1']
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vakoms',
        'USER': 'root',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '3306',
        'CONN_MAX_AGE': 60 * 10,  # 10 minutes
    }
}

