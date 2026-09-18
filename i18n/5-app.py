#!/usr/bin/env python3
"""Flask app mocking user login to greet the visitor in their language."""
from typing import Optional, Dict, Union

from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """Configuration holding the supported languages and defaults."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel()


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Optional[Dict[str, Union[str, None]]]:
    """Return the user matching the login_as URL parameter, or None."""
    login_as = request.args.get("login_as")
    if login_as is None:
        return None
    try:
        return users.get(int(login_as))
    except ValueError:
        return None


@app.before_request
def before_request() -> None:
    """Set the logged-in user as a global before handling the request."""
    g.user = get_user()


def get_locale() -> Optional[str]:
    """Return the locale from the URL parameter or request headers."""
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


@app.route("/", strict_slashes=False)
def index() -> str:
    """Render the home page with translated messages."""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
