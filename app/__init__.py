import os
from flask import Flask
from flask_cors import CORS
from flask_babel import Babel
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail

from config import BASE_DIR
from .base.utils import send_email_after_500_error


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

mail = Mail(app)

toolbar = DebugToolbarExtension(app)

# send mail if 500 error
if not app.debug:
    send_email_after_500_error(app)

from .base.utils import momentjs

app.jinja_env.globals['momentjs'] = momentjs


from .base import views
from .auth.views import auth
from .posts.views import posts

app.register_blueprint(auth)
app.register_blueprint(posts)
