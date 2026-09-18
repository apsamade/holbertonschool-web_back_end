# User authentication service

A learning project that walks through building a user authentication
mechanism from scratch with Flask, SQLAlchemy and bcrypt.

## Modules

- `user.py` — SQLAlchemy `User` model mapped to the `users` table.
- `db.py` — `DB` class handling database access (add/find/update users).
- `auth.py` — `Auth` class holding the authentication logic.
- `app.py` — Flask application exposing the API routes.

## Notes

The Flask app only interacts with `Auth`, never with `DB` directly.
Only public methods of `Auth` and `DB` are used outside these classes.
