#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import  NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session
    
    def add_user(self, email: str, hashed_password: str) -> User:
        """Return and add user to db
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()

        return user


    def find_user_by(self,is_Update: bool=False, **kwargs: dict) -> User:
        """no explanation needed
        """
        columns =  ["email", "hashed_password", "id", "session_id", "reset_token"] 
        if all(e not in columns for e in kwargs.keys()):
            raise InvalidRequestError
        
        user = self._session.query(User).filter_by(**kwargs)
        if user.first() is None:
            raise NoResultFound
        elif is_Update:
            return user

        return user.first()
        

    def update_user(self, user_id: int, **kwargs: dict) -> None:
        """func
        """
        try:
            user = self.find_user_by(is_Update=True,id=user_id)
        except (InvalidRequestError, NoResultFound) as e:
            raise ValueError
        
        user.update({**kwargs})