#!/usr/bin/env python3
"""Flask app that selects the request locale from Accept-Language headers."""
from typing import Optional

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration holding the supported languages and defaults."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel()


def get_locale() -> Optional[str]:
    """Return the best matching language from the request headers."""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


@app.route("/", strict_slashes=False)
def index() -> str:
    """Render the home page."""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
