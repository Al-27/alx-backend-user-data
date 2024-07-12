#!/usr/bin/env python3
""" Module of Index views
"""
from typing import List, TypeVar
from flask import request
from api.v1.auth import Auth

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
            if type(authorization_header) == type(str):
                if authorization_header[:6] == "Basic ":
                    return authorization_header[6:]
        return None