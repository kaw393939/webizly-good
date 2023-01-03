from flask import Blueprint, render_template, current_app

from application.database import User

bp_homepage = Blueprint('homepage', __name__, template_folder='templates')


@bp_homepage.route('/')
def homepage():
    with current_app.app_context():
        current_app.logger.info('Log It')

    return render_template('homepage.html')


@bp_homepage.route('/about')
def about():
    return render_template('about.html')

