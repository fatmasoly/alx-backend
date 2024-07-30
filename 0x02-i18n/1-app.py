#!/usr/bin/env python3
"""flask app"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object('Config')


@app.route('/', strict_slashes=False)
def index() -> str:
    """index page"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
