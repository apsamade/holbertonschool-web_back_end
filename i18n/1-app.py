#!/usr/bin/env python3
"""Flask application configured with Flask-Babel for i18n support."""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Configuration holding the supported languages and defaults."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/", strict_slashes=False)
def index() -> str:
    """Render the home page."""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
