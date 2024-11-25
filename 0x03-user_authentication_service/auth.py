#!/usr/bin/env python3
"""Hash password"""


import bcrypt
from db import DB
from user import User
import base64
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _generate_uuid():
    """Generate UUIDs"""
    return str(uuid.uuid4())


def _hash_password(password: str) -> bytes:
    """
    _has_passward method takes in a password string args
    and returns bytes
    """
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(password.encode("utf-8"), salt)

    return hashed_pwd


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a user and return a user object"""
        try:
            existing_user = self._db.find_user_by(email=email)
            if existing_user:
                raise ValueError(f"User {email} already exists")

        except NoResultFound:
            hashed_pwd = _hash_password(password)
            new_user = self._db.add_user(email, hashed_pwd)
            return new_user

        except InvalidRequestError:
            raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        """Credential validation method"""
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode("utf-8"), user.hashed_password):
                return True
            else:
                return False

        except (InvalidRequestError, NoResultFound):
            return False
