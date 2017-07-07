from flask import (abort, Blueprint, render_template, redirect, url_for,
                   session, logging, request, flash, g)
from flask_babel import gettext as _
from flask_login import login_user, logout_user, login_required
from flask_mail import Message

from app import app, db, login_manager, mail
from .forms import RegisterForm, LoginForm
from .models import User
from ..base.utils import is_safe_url


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        form.populate_obj(user)
        user.password = User.hash_password(user.password)
        db.session.add(user)
        db.session.commit()
        # msg = Message(app.config['SITE_NAME'],
        #               sender=app.config['ADMINS'][0],
        #               recipients=[user.email])
        # msg.body = 'Спасибо что зарегистрировались'

        msg = Message(app.config['SITE_NAME'],
                      sender=app.config['ADMINS'][0],
                      recipients=[user.email],
                      html=render_template('email/register.html', username=user.username))
        mail.send(msg)
        login_user(user)
        return redirect(url_for('home'))
    return render_template('auth/register.html', form=form)


@auth.route('/profile')
@login_required
def profile():
    return render_template('auth/profile.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        login_user(form.getUser(), form.remember_me.data)
        flash(_('Вы успешно вошли.'), 'success')
        next = request.args.get('next')
        if not is_safe_url(next):
            return abort(400)

        return redirect(next or url_for('home'))
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
