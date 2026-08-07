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
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if not path.endswith('/'):
            path += '/'
        for excluded in excluded_paths:
            if excluded.endswith('*'):
                if path.startswith(excluded[:-1]):
                    return False
            elif path == excluded:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Return the Authorization header from a request object
        """
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Return the current authenticated user
        """
        return None
