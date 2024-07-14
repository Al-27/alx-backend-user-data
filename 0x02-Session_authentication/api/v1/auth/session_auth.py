#!/usr/bin/env python3
""" Module of Index views
"""
from typing import List, TypeVar
from flask import request
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """Class
    """
    user_id_by_session_id = dict()

    def create_session(self, user_id: str = None) -> str:
        """func - creates a Session ID for a user_id
        """
        if user_id:
            if isinstance(user_id, str):
                uid = str(uuid.uuid4())
                self.user_id_by_session_id.update({uid: user_id})
                return uid
        return None
    

    def user_id_for_session_id(self, session_id: str = None) -> str: 
        """get id
        """
        if session_id:
            if isinstance(session_id, str):
                return self.user_id_by_session_id.get(session_id)                
        return None