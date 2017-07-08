from flask import render_template, send_from_directory, request, g, make_response
from flask_login import current_user

from app import app, babel, db


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'].keys())


@app.before_request
def before_request():
    g.user = current_user
    locale = get_locale()
    if not locale:
        g.locale = app.config['DEFAULT_LOCALE']
    else:
        g.locale = locale


@app.context_processor
def inject_dict_for_all_templates():
    vars = {
        'site_name': app.config['SITE_NAME'],
    }
    return dict(app=vars)


@app.route('/node_modules/<path:path>')
def send_node_modules(path):
    return send_from_directory('node_modules', path)


@app.errorhandler(404)
def not_found_error(e):
    print(e)
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('errors/500.html'), 500


@app.route('/')
def home():
    return render_template('base/home.html')


@app.route('/about')
def about():
    return render_template('base/about.html')


@app.route('/contact')
def contact():
    return render_template('base/contact.html')

