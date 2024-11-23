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

        try:
            user_found = self._session.query(User).filter_by(**kwargs).one()
            return user_found
        except NoResultFound:
            raise NoResultFound("No user found")
        except InvalidRequestError as e:
            raise InvalidRequestError(f"Invalid query: {e}")

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update a user by it's id"""
        try:
            user = self.find_user_by(id=user_id)
            for k, v in kwargs.items():
                if hasattr(user, k):
                    setattr(user, k, v)
                else:
                    raise ValueError()

            self._session.commit()

        except NoResultFound:
            raise ValueError("User not found.")
        except InvalidRequestError as e:
            raise ValueError(f"Invalid request: {str(e)}")
        except Exception as e:
            raise ValueError(f"An unexpected error occured: {str(e)}")
