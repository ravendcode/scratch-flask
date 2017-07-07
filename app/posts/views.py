from flask import Blueprint, render_template, request, redirect, url_for, g
from werkzeug.exceptions import abort
from flask_login import login_required

from app import app, db
from .forms import PostCreateForm
from .models import Post
from ..auth.models import User

posts = Blueprint('posts', __name__, url_prefix='/posts')


@posts.route('/')
def post_list():
    posts = Post.query.all()
    return render_template('posts/post_list.html', posts=posts)


@posts.route('/<int:id>')
def post_detail(id):
    post = Post.query.get_or_404(id)
    x
    return render_template('posts/post_detail.html', post=post)


@posts.route('/create', methods=['GET', 'POST'])
@login_required
def post_create():
    form = PostCreateForm(request.form)
    if form.validate_on_submit():
        post = Post()
        form.populate_obj(post)
        post.create_slug()
        post.user = g.user
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('posts.post_list'))
    return render_template('posts/post_create.html', form=form)
