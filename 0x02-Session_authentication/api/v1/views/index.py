#!/usr/bin/env python3
"""
Module for Index views
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """
    GET /api/v1/status
    Return: - status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """
    GET /api/v1/stats
    Return:- number of all objects
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def test_forbidden() -> str:
    """
    GET /api/v1/forbidden
    Return: - Raise any error
    """
    return abort(403)


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def test_unathourized() -> str:
    """
    GET /api/v1/unauthorized
    Return: Raise any error
    """
    return abort(401)
