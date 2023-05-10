
import hashlib
import hmac
import secrets

from . import config

def gen_salt(length: int) -> str:
    """Generate a random string of SALT_CHARS with specified ``length``."""
    if length <= 0:
        raise ValueError("Salt length must be positive")

    return "".join(secrets.choice(config.LOGIN_SALT_CHARS) for _ in range(length))

def _hash_internal(method: str, salt: str, password: str) -> tuple[str, str]:
    """Internal password hash helper.  Supports plaintext without salt,
    unsalted and salted passwords.  In case salted passwords are used
    hmac is used.
    """
    if method == "plain":
        return password, method

    salt_b = salt.encode("utf-8")
    password_b = password.encode("utf-8")

    if method.startswith("pbkdf2:"):
        if not salt:
            raise ValueError("Salt is required for PBKDF2")

        args = method[7:].split(":")

        if len(args) not in (1, 2):
            raise ValueError("Invalid number of arguments for PBKDF2")

        method = args.pop(0)
        iterations = int(args[0] or 0) if args else config.LOGIN_DEFAULT_PBKDF2_ITERATIONS
        return (
            hashlib.pbkdf2_hmac(method, password_b, salt_b, iterations).hex(),
            f"pbkdf2:{method}:{iterations}",
        )

    if salt:
        return hmac.new(salt_b, password_b, method).hexdigest(), method

    return hashlib.new(method, password_b).hexdigest(), method

def generate_password_hash(
    password: str, method: str = "pbkdf2:sha256", salt_length: int = 16
) -> str:
    """Hash a password with the given method and salt with a string of
    the given length. The format of the string returned includes the method
    that was used so that :func:`check_password_hash` can check the hash.
    The format for the hashed string looks like this::
        method$salt$hash
    This method can **not** generate unsalted passwords but it is possible
    to set param method='plain' in order to enforce plaintext passwords.
    If a salt is used, hmac is used internally to salt the password.
    If PBKDF2 is wanted it can be enabled by setting the method to
    ``pbkdf2:method:iterations`` where iterations is optional::
        pbkdf2:sha256:80000$salt$hash
        pbkdf2:sha256$salt$hash
    :param password: the password to hash.
    :param method: the hash method to use (one that hashlib supports). Can
                   optionally be in the format ``pbkdf2:method:iterations``
                   to enable PBKDF2.
    :param salt_length: the length of the salt in letters.
    """
    salt = gen_salt(salt_length) if method != "plain" else ""
    h, actual_method = _hash_internal(method, salt, password)
    return f"{actual_method}${salt}${h}"

def check_password_hash(pwhash: str, password: str) -> bool:
    """Check a password against a given salted and hashed password value.
    In order to support unsalted legacy passwords this method supports
    plain text passwords, md5 and sha1 hashes (both salted and unsalted).
    Returns `True` if the password matched, `False` otherwise.
    :param pwhash: a hashed string like returned by
                   :func:`generate_password_hash`.
    :param password: the plaintext password to compare against the hash.
    """
    if pwhash.count("$") < 2:
        return False

    method, salt, hashval = pwhash.split("$", 2)
    return hmac.compare_digest(_hash_internal(method, salt, password)[0], hashval)