#!/usr/bin/env python3
"""
Hash Password Encryption and Validation
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Receives a string argument name 'password' and returns
    a salted, hashed password, which is a byte string.

    Args:
        password (str): password

    Returns:
        bytes: encryption password
    """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Checks password

    Args:
        hashed_password (bytes): hash
        password (str): password

    Returns:
        bool: true or false
    """
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid
