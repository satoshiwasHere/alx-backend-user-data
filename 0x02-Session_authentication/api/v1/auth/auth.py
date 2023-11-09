#!/usr/bin/env python3
"""
Authentication Module
"""
from os import getenv
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Authentication Class
    """

    def __init__(self):
        """
            Constructor class

            Args:
            path: authentication path
            excluded_paths: excluded path to authenticate
        """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            Require the auth

            Args:
            path: authentication path
            excluded_paths: excluded path to authenticate

            Return: True if authenticated otherwise false
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path[-1] is not '/':
            path += '/'

        for paths in excluded_paths:
            if paths.endswith('*'):
                if path.startswith(paths[:-1]):
                    return False
            elif path == paths:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
            identify the headers

            Args:
            request: identify the autthorization

            Return: authorization header or Null
        """
        if request is None:
            return None

        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
            search current user

            Args:
            request: search the requested user

            Return: the user
        """
        return None

    def session_cookie(self, request=None):
        """
            analysis of the cookie value

            Args:
                request: Get the cookie session

            Return: the cookie session
        """
        if request is None:
            return None

        session_env = getenv('SESSION_NAME', None)
        cookie_sess = request.cookies.get(session_env, None)

        return cookie_sess
