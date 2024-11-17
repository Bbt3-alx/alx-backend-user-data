#!/usr/bin/env python3
"""Empty Session"""


from flask import session
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """A new authentication mechanisme"""
    pass
