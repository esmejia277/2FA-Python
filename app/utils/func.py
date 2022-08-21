
import qrcode
import os
from secrets import choice

def generate_secret() -> str:  # Function to return a random string with length 16.
    secret: str = ''
    while len(secret) < 16:
        secret += choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ234567')
    return secret