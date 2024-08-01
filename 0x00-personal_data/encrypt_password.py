#!/usr/bin/env python3
"""
Password Encryption and Validation Module.

This module provides functions to generate salted and hashed passwords
and to validate passwords against hashed values.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Generate a salted and hashed password.

    Args:
        password (str): A string containing the plain text password to be hashed.

    Returns:
        bytes: A byte string representing the salted, hashed password.
    """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validate whether the provided password matches the hashed password.

    Args:
        hashed_password (bytes): A byte string representing the salted, hashed password.
        password (str): A string containing the plain text password to be validated.

    Returns:
        bool: True if the provided password matches the hashed password, False otherwise.
    """
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid


