#!/usr/bin/env python3
"""Flask app inferring both locale and timezone from URL/user/defaults."""
from typing import Optional, Dict, Union

import pytz
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
    """Return the locale from URL, user settings, then request headers."""
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    if g.get("user") and g.user.get("locale") in app.config["LANGUAGES"]:
        return g.user.get("locale")
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_timezone() -> str:
    """Return a validated timezone from URL, user settings, or the default."""
    timezone = request.args.get("timezone")
    if timezone is None and g.get("user"):
        timezone = g.user.get("timezone")
    if timezone:
        try:
            return str(pytz.timezone(timezone))
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    return app.config["BABEL_DEFAULT_TIMEZONE"]


babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route("/", strict_slashes=False)
def index() -> str:
    """Render the home page with translated messages."""
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
