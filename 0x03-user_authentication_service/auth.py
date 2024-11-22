#!/usr/bin/env python3
"""Hash password"""


import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """
    _has_passward method takes in a password string args
    and returns bytes
    """
    hashed_pwd = bcrypt.hashpw(password, salt)

    return hashed_pwd


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a user and return a user object"""
        if self._db.find_user_by(email=email):
            raise ValueError(f"User {email} already exists")
        else:
            hashed_pwd = _hash_password(password)
            new_user = self._db.add_user(email, hashed_pwd)
            return new_user
