#!/usr/bin/env python3
"""Basic Flask application for the authentication service."""
from flask import Flask, jsonify, request, abort

from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """Return a welcome JSON payload for the root route."""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users() -> str:
    """Register a user from form data or report an existing email."""
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    return jsonify({"email": email, "message": "user created"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
