#!/usr/bin/env python3
""" Module of Auth
"""
from bcrypt import hashpw,gensalt,checkpw
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """hash
    """
    byt = hashpw(bytes(password, 'utf-8'), gensalt() )
    return byt

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """func
        """
        self._db = DB()


    def _generate_uuid(self) -> str:
        """priv meth
        """
        import uuid
        return str(uuid.uuid4())

    def register_user(self, email: str, password: str) -> User:
        """reg
        """
        try:
            user = self._db.find_user_by(email=email)
        except:
            user = None            

        if user :
            raise ValueError(f"User {email} already exists")
        
        hashed_password = _hash_password(password)
        user = self._db.add_user(email,hashed_password)
        return user


    def valid_login(self, email: str, password: str) -> bool:
        """check
        """
        try:
            user = self._db.find_user_by(email=email)
        except:
            return False
        
        return checkpw(bytes(password,"utf-8"),user.hashed_password)


    def create_session(self, email: str) -> str:
        """sess
        """
        try:
            user = self._db.find_user_by(email=email)
        except:
            return None
        
        user.session_id = self._generate_uuid()
        self._db.update_user(user.id,session_id=user.session_id)
        return user.session_id
    
    def get_user_from_session_id(self, session_id: str) -> User:
        """func
        """
        try:
            user = self._db.find_user_by(session_id=session_id)
        except:
            return None
        
        return user
