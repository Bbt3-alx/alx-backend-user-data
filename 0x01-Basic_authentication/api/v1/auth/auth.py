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
        elif excluded_paths is None or len(excluded_paths) == 0:
            return True
        elif path in excluded_paths or path + '/' in excluded_paths:
            return False


    def authorization_header(self, request=None) -> str:
        """The authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """The current user"""
        return None
