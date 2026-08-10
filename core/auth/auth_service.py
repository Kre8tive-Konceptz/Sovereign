"""
Authentication Service - Refactored for Security
Migrated from MD5 to bcrypt + JWT tokens
"""
import bcrypt
import jwt
import os
from datetime import datetime, timedelta
from typing import Dict, Optional

class AuthService:
    def __init__(self):
        self.secret_key = os.getenv('JWT_SECRET', 'c25-sovereign-key-change-in-production')
        self.algorithm = 'HS256'
        self.token_expiry_hours = 24
    
    def hash_password(self, password: str) -> str:
        """Hash password using bcrypt with salt"""
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
    
    def verify_password(self, password: str, hashed: str) -> bool:
        """Verify password against hash"""
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
    
    def generate_token(self, user_id: str, role: str = 'user') -> str:
        """Generate JWT token"""
        payload = {
            'user_id': user_id,
            'role': role,
            'exp': datetime.utcnow() + timedelta(hours=self.token_expiry_hours),
            'iat': datetime.utcnow()
        }
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
    
    def verify_token(self, token: str) -> Optional[Dict]:
        """Verify and decode JWT token"""
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
    
    def refresh_token(self, token: str) -> Optional[str]:
        """Refresh expired token"""
        payload = self.verify_token(token)
        if payload:
            return self.generate_token(payload['user_id'], payload.get('role', 'user'))
        return None

if __name__ == "__main__":
    auth = AuthService()
    print("AuthService initialized with bcrypt + JWT")
