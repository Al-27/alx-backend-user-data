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
        import codecs
        try:
            if base64_authorization_header:
                if isinstance(base64_authorization_header, str):
                    return codecs.decode(base64_authorization_header)
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