#!/usr/bin/env python3
""" Module of Index views
"""
from typing import List, TypeVar
from flask import request
from api.v1.auth.auth import Auth

class BasicAuth(Auth):
    """Class
    """
    
    def __init__(self):
        """function
        """
        pass
    
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """function
        """
        if authorization_header:
            if isinstance(authorization_header, str):
                if authorization_header[:6] == "Basic ":
                    return authorization_header[6:]
        return None
    
    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str: 
        """function
        """
        import base64
        try:
            if base64_authorization_header:
                if isinstance(base64_authorization_header, str):
                    return base64.b64decode(base64_authorization_header).decode("utf-8")
        except Exception as e:
            pass

        return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """function
        """
        if decoded_base64_authorization_header:
            if isinstance(decoded_base64_authorization_header, str):
                if len(decoded_base64_authorization_header.split(":")) == 2:
                    return tuple(decoded_base64_authorization_header.split(":"))
        return (None,None)

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'): 
        """func
        """
        from models.user import User
        if user_email and isinstance(user_email, str) and user_pwd and isinstance(user_pwd,str):
            user = User.search({"email": user_email})
            if len(user) == 1 :
                if user[0].is_valid_password(user_pwd):
                    return user[0]
        return None
        