#!/usr/bin/env python3
""" Module that manages the API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Template for all authentication systems of the API
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determine if a given path requires authentication
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Return the Authorization header from a request object
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Return the current authenticated user
        """
        return None
