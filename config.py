"""App config"""

import os

# import binascii
# token = binascii.hexlify(os.urandom(24)).decode()
SITE_NAME = 'Scratch Flask'
BASE_DIR = os.path.dirname(__file__)
ENV = os.environ.get('ENV', 'production')
# ENV = 'production'
DEBUG = True if ENV == 'development' else False
HOST = '0.0.0.0'
PORT = 3000
DEBUG_TB_INTERCEPT_REDIRECTS = False
SECRET_KEY = os.environ.get(
    'SECRET_KEY', 'df6019219400b9b588b91d19d91e050bebab072af5fa9d22')
# SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
# SQLALCHEMY_DATABASE_URI = 'postgresql://yourusername:yourpassword@localhost/yournewdb'
SQLALCHEMY_DATABASE_URI = os.environ.get(
    'DATABASE_URL', 'mysql+pymysql://root:qwerty@localhost/scratch_flask')
SQLALCHEMY_TRACK_MODIFICATIONS = False
LANGUAGES = {
    'en': 'English',
    'ru': 'Russian'
}
DEFAULT_LOCALE = 'ru'
BABEL_DEFAULT_LOCALE = 'ru'

MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None
MAIL_USE_TLS = False
MAIL_USE_SSL = False
# administrator list
ADMINS = ['admin@email.com']

# gmail
# MAIL_SERVER = 'smtp.googlemail.com'
# MAIL_PORT = 465
# MAIL_USE_TLS = False
# MAIL_USE_SSL = True
# MAIL_USERNAME = 'your-gmail-username'
# MAIL_PASSWORD = 'your-gmail-password'
# ADMINS = ['admin@gmail.com']
