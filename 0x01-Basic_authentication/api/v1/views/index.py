#!/usr/bin/env python3
"""
Index views module
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def authorized() -> str:
    """
    GET /api/v1/unauthorized
    Return: 401 error
    """
    abort(401, description="Unauthorized")


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbid() -> str:
    """
    GET /api/v1/forbidden
    Return: 403 error
    """
    abort(403, description="Forbidden")


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """
    GET /api/v1/status
    Return: - api status
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """
    GET /api/v1/stats
    Return: number of each objects
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)
