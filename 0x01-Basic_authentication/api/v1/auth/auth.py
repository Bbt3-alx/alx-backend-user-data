#!/usr/bin/env python3
"""Auth class"""


from flask import request
from typing import List, TypeVar


class Auth:
    """Class authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """The require path"""
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        path = path.rstrip('/')
        excluded_paths = [p.rstrip('/') for p in excluded_paths]

        if path in excluded_paths:
            return False
        else:
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
