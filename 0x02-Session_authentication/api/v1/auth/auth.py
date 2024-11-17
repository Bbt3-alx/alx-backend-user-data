#!/usr/bin/env python3
"""Auth class"""


from flask import request
from typing import List, TypeVar
import fnmatch
from os import getenv


class Auth:
    """Class authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """The require path"""
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        if not path.endswith('/'):
            path += '/'

        for pattern in excluded_paths:
            # Normalize the pattern to ensure it ends with slash
            if not pattern.endswith('/'):
                pattern += '/'

            # Use fnmatch to check if the path matches the pattern
            if fnmatch.fnmatch(path, pattern):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """The authorization header"""
        if request is None or 'Authorization' not in request.headers:
            return None
        else:
            return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """The current user"""
        return None

    def session_cookie(self, request=None):
        """Session cookie - returns a cookie value from a request"""
        if not request:
            return None

        cookie_name = getenv('SESSION_NAME')
        if not cookie_name:
            return None

        return request.cookies.get(cookie_name)
