#!/usr/bin/env python3
"""Module for hashing passwords and validating them with bcrypt."""
import bcrypt


def hash_password(password: str) -> bytes:
    """Return a salted, hashed byte string for the given password."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Return whether the password matches the given hashed password."""
    return bcrypt.checkpw(password.encode(), hashed_password)
