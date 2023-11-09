#!/usr/bin/env python3
"""
UserSession model
"""
import hashlib
from models.base import Base


class UserSession(Base):
    """
    The User class
    """
    def __init__(self, *args: list, **kwargs: dict):
        """
        The Constructor class
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
