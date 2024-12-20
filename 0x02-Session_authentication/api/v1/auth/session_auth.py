#!/usr/bin/env python3
"""Empty Session"""


from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """A new authentication mechanisme"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Return a User ID based on a Session ID"""
        if not session_id or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Use session ID for identifying a User"""
        cookie_value = self.session_cookie(request)
        user_id = self.user_id_for_session_id(cookie_value)
        if user_id is None:
            return None
        return User.get(user_id)
