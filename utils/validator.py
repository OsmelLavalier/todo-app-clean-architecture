import re

import bcrypt


def validate_username(username: str) -> bool:
    if not re.match("^[a-zA-Z0-9_-]+$", username):
        return False
    return True


def hash_password(password: str) -> bytes:
    byte_pass = password.encode("utf-8")
    return bcrypt.hashpw(byte_pass, bcrypt.gensalt())


def is_same_password(password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)
