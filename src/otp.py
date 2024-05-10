import hashlib
import time


def generate_otp(secret_key, interval=300, length=6):
    """
    Generate a time-based OTP using SHA-256 hashing algorithm.

    Args:
    secret_key (str): Secret key used for hashing.
    interval (int): Time interval in seconds for OTP validity. Default is 300 seconds (5 minutes).
    length (int): Length of OTP. Default is 6 (6 digits). Maximum 8 digits.

    Returns:
    str: Generated OTP.
    """
    length = length if length < 9 else 6
    current_time = int(time.time() / interval)
    otp_hash = hashlib.sha256((str(current_time) + secret_key).encode()).hexdigest()
    otp_numeric = ''.join(char for char in otp_hash if char.isdigit())
    return otp_numeric[:length]  # Return the first length characters as the OTP
