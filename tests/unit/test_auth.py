"""Unit tests for authentication module"""
import pytest
from core.auth import AuthService

def test_password_hashing():
    auth = AuthService()
    password = "test_password_123"
    hashed = auth.hash_password(password)
    assert auth.verify_password(password, hashed)
    assert not auth.verify_password("wrong_password", hashed)

def test_token_generation():
    auth = AuthService()
    token = auth.generate_token("user123", "admin")
    assert token is not None
    payload = auth.verify_token(token)
    assert payload['user_id'] == "user123"
    assert payload['role'] == "admin"

def test_token_expiry():
    auth = AuthService()
    auth.token_expiry_hours = 0  # Immediate expiry
    token = auth.generate_token("user123")
    payload = auth.verify_token(token)
    assert payload is None  # Should be expired
