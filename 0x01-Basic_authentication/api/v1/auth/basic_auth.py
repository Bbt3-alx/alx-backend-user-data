#!/usr/bin/env python3
"""Basic auth"""


import base64
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
