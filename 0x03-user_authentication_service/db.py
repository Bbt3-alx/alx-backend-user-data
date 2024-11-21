#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from typing import Optional

from user import Base, User


class DB:
    """DB class"""

    def __init__(self) -> None:
        """Initialize a new DB instance"""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add and asave a new User object"""
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()

        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        This method takes in arbitrary keyword arguments
        and returns the first row found in the users table
        as filtered by the method’s input arguments.
        """
        user_found = self._session.query(User).filter_by(**kwargs).one()
        if user_found:
            return user_found
        elif InvalidRequestError:
            raise InvalidRequestError
        else:
            raise NoResultFound

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update a user by it's id"""
        user = self.find_user_by(id=user_id)
        if user:
            for k, v in kwargs.items():
                try:
                    user.k = v
                except ValueError:
                    raise
            self._session.add(user)
            self._session.commit()
        else:
            return None
