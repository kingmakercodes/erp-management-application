import secrets

"""
Generates a 32-character secret key
"""

print(secrets.token_urlsafe(32))