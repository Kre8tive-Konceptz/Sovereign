"""Authentication Service - bcrypt + JWT"""
import bcrypt
import jwt
import os
from datetime import datetime, timedelta

class AuthService:
    def __init__(self):
        self.secret_key = os.getenv('JWT_SECRET', 'c25-sovereign-key')
        self.algorithm = 'HS256'
    
    def hash_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
    
    def verify_password(self, password: str, hashed: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
    
    def generate_token(self, user_id: str, role: str = 'user') -> str:
        payload = {
            'user_id': user_id,
            'role': role,
            'exp': datetime.utcnow() + timedelta(hours=24),
            'iat': datetime.utcnow()
        }
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
    
    def verify_token(self, token: str):
        try:
            return jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
        except:
            return None
