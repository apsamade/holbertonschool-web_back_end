#!/usr/bin/env python3
"""Authentication module handling password hashing and user registration."""
import uuid

import bcrypt
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Return a salted bcrypt hash of the given password as bytes."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Return a string representation of a newly generated UUID."""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Initialize a new Auth instance with a database connection."""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register and return a new user, or raise if the email exists."""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed = _hash_password(password)
            return self._db.add_user(email, hashed)
        raise ValueError("User {} already exists".format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """Return True if the email/password pair matches a stored user."""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        return bcrypt.checkpw(password.encode("utf-8"), user.hashed_password)

    def create_session(self, email: str) -> str:
        """Create a session for the user and return the session ID."""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id
