import wtforms as f
from wtforms.validators import ValidationError
from sqlalchemy import or_

from app import db
from ..base.forms import BaseForm, Unique
from ..auth.models import User


class RegisterForm(BaseForm):
    username = f.StringField('Имя пользователя', [
                             f.validators.Length(min=2, max=25),
                             Unique(model=User)])
    email = f.StringField('Email', [f.validators.Length(min=2, max=25),
                                    f.validators.Email(),
                                    Unique(model=User)])
    password = f.PasswordField(
        'Пароль', [f.validators.DataRequired(),
                   f.validators.EqualTo(
            'confirm_password', 'Поле должно быть равно полю потвердите пароль.'),
            f.validators.Length(min=6, max=25)])
    confirm_password = f.PasswordField(
        'Потвердите пароль', [f.validators.DataRequired()])


class LoginForm(BaseForm):
    username_or_email = f.StringField('Имя пользователя или  email', [
                                      f.validators.DataRequired()])
    password = f.PasswordField('Пароль', [f.validators.DataRequired()])
    remember_me = f.BooleanField('remember_me', default=False)

    def getUser(self):
        username_or_email = self.username_or_email.data
        user = User.query.filter(
            or_(User.username == username_or_email, User.email == username_or_email)).first()
        return user

    def validate(self):
        if not BaseForm.validate(self):
            return False
        user = self.getUser()
        if not user:
            self.username_or_email.errors.append(
                'Неверное имя пользователя или email.')
            return False
        else:
            if user.check_password(self.password.data):
                return True
            else:
                self.password.errors.append('Неверный пароль.')
                return False
        return True
