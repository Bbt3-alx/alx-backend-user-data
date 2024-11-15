#!/usr/bin/env python3
"""Basic auth"""


import base64
import re
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.base import Base
from models.user import User


class BasicAuth(Auth):
    """Basic auth class"""
    def extract_base64_authorization_header(
            self,
            authorization_header: str
            ) -> str:
        """Returns the Base64 part of the Authorization header"""
        is_str = isinstance(authorization_header, str)
        if authorization_header and is_str:
            start_b = authorization_header.startswith('Basic' + ' ')

            if start_b:
                basic_k_v = authorization_header.split(' ')
                return basic_k_v[1]
            return None
        return None

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str
            ) -> str:
        """Basic - Base64 decode"""
        base64_pattern = re.compile(r'^[A-Za-z0-9+/]+={0,2}$')

        is_str = isinstance(base64_authorization_header, str)
        if not base64_authorization_header or not is_str:
            return None

        if not base64_pattern.match(base64_authorization_header):
            return None

        try:
            d = base64.b64decode(base64_authorization_header).decode('utf-8')
            return d
        except Exception:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
            ) -> (str, str):
        """Basic - User credentials"""
        d_b64_auth_h = decoded_base64_authorization_header
        if d_b64_auth_h:
            if isinstance(d_b64_auth_h, str) and d_b64_auth_h.count(':') == 1:
                credentials = d_b64_auth_h.split(':')
                return (credentials[0], credentials[1])
            return (None, None)
        return (None, None)

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str
            ) -> TypeVar('User'):
        """
        Basic - User object:
        that returns the User instance
        based on his email and password.
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        # Search for the user by email
        users = User.search({'email': user_email})
        if not users:
            return None

        # Check if the password is valid
        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None

        return user
