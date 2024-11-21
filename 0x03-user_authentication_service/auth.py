#!/usr/bin/env python3
"""Hash password"""


import bcrypt


def _hash_password(password: str) -> bytes:
    """
    _has_passward method takes in a password string args
    and returns bytes
    """
    hashed_pwd = bcrypt.hashpw(password, salt)

    return hashed_pwd
