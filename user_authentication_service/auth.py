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

    def get_user_from_session_id(self, session_id: str) -> User:
        """Return the user tied to the given session ID, or None."""
        if session_id is None:
            return None
        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Reset the given user's session ID to None."""
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """Generate and store a reset password token for the user."""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError()
        reset_token = _generate_uuid()
        self._db.update_user(user.id, reset_token=reset_token)
        return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """Update the user's password using a valid reset token."""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError()
        hashed = _hash_password(password)
        self._db.update_user(
            user.id, hashed_password=hashed, reset_token=None)
