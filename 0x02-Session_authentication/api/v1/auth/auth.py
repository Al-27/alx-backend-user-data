#!/usr/bin/env python3
""" Module of Index views
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """Class
    """
    def __init__(self) -> None:
        """function
        """
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """function
        """
        if path:
            tmp = '/'+path.strip('/')
            if tmp in excluded_paths or f'{tmp}/' in excluded_paths:
                return False
        return True 

    def authorization_header(self, request=None) -> str:
        """function
        """
        if request:
            if "Authorization" in request.keys():
                return request["Authorization"]
        return None
    
    def current_user(self, request=None) -> TypeVar('User'): # type: ignore
        """function
        """
        return None


    def session_cookie(self, request=None):
        """get me some cookies
        """
        import os
        cookie_nm = "_my_session_id"
        if os.getenv("SESSION_NAME"):
            cookie_nm = os.getenv("SESSION_NAME")
        if request and request.cookie:
            return request.cookie.get(cookie_nm)

        return None
