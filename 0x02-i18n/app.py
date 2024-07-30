#!/usr/bin/env python3
"""flask app"""

from flask import Flask, render_template
import datetime
from flask_babel import Babel, format_datetime


class Config:
    """Config class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object('config')
