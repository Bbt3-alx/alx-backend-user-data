#!/usr/bin/env python3
"""Basic auth"""


import base64
import re
from api.v1.auth.auth import Auth


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
