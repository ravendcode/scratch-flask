import os
from flask import Flask
from flask_cors import CORS
from flask_babel import Babel
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_debugtoolbar import DebugToolbarExtension

from config import (BASE_DIR, MAIL_PASSWORD, MAIL_PORT,
                    MAIL_SERVER, MAIL_USERNAME, ADMINS)


app = Flask(__name__, root_path=BASE_DIR)
app.config.from_object('config')
print('ENV is {}'.format(app.config['ENV']))

CORS(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

babel = Babel(app)

db = SQLAlchemy(app)

toolbar = DebugToolbarExtension(app)

# send mail if 500 error
if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    credentials = None
    if MAIL_USERNAME or MAIL_PASSWORD:
        credentials = (MAIL_USERNAME, MAIL_PASSWORD)
    mail_handler = SMTPHandler((MAIL_SERVER, MAIL_PORT), 'no-reply@' +
                               MAIL_SERVER, ADMINS, app.config['SITE_NAME'], credentials)
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)


from .base.utils import momentjs

app.jinja_env.globals['momentjs'] = momentjs


from .base import views
from .auth.views import auth
from .posts.views import posts

app.register_blueprint(auth)
app.register_blueprint(posts)
