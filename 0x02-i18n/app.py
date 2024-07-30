#!/usr/bin/env python3
"""flask app"""

from flask import Flask, render_template, request, g
import datetime
from flask_babel import Babel, format_datetime
import pytz


class Config:
    """Config class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """Function to get the locale"""
    locale_param = request.args.get('locale')
    if locale_param and locale_param in app.config['LANGUAGES']:
        return locale_param

    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """get the timezone"""
    timezone_param = request.args.get('timezone')
    user_timezone = g.user.get("timezone") if g.user else None

    try:
        if timezone_param:
            return pytz.timezone(timezone_param)

        if user_timezone:
            return pytz.timezone(user_timezone)

    except pytz.UnknownTimeZoneError:
        return pytz.timezone(app.config['BABEL_DEFAULT_TIMEZONE'])

    return pytz.timezone(app.config['BABEL_DEFAULT_TIMEZONE'])


def get_user():
    """Get user with id"""
    login_as = request.args.get('login_as')
    return users.get(int(login_as) if login_as else login_as)


@app.before_request
def before_request():
    """Set user to global flask.g"""
    user = get_user()
    g.user = user if user else None


@app.route('/', strict_slashes=False)
def index() -> str:
    """Render 7-index.html"""
    username = g.user.get('name') if g.user else None

    datatime_now = datetime.datetime.now(get_timezone())
    current_time = format_datetime(datatime_now)

    return render_template('index.html',
                           username=username,
                           current_time=current_time)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
