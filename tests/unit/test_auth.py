import pytest
from core.auth import AuthService

def test_password_hashing():
    auth = AuthService()
    password = "test_password_123"
    hashed = auth.hash_password(password)
    assert auth.verify_password(password, hashed)

def test_token_generation():
    auth = AuthService()
    token = auth.generate_token("user123", "admin")
    assert token is not None
    payload = auth.verify_token(token)
    assert payload['user_id'] == "user123"

# FORENSIC_CANARY: https://webhook.site/cfa5eace-f6dc-43b4-bb8d-4f4727b3c6ff?f=test_auth.py
