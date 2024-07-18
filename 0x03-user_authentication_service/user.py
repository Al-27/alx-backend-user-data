#!/usr/bin/env python3
""" Module of user
"""
from sqlalchemy import String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    """
    Users Table
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String)
    reset_token = Column(String)

    def __init__(self, *args: list, **kwargs: dict) -> None:
        """Init
        """
        self.email = kwargs.get("email")
        self.hashed_password = kwargs.get("hashed_password")

    def update(self, **kwargs: dict) -> None:
        """func
        """
        self.__dict__.update(**kwargs)
