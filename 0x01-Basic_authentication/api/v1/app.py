#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


auth = None

AUTH_TYPE = getenv('AUTH_TYPE')
if AUTH_TYPE == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()
elif AUTH_TYPE == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """Error handler: Unauthorized"""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """Error handler: Forbidden"""
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def filter_request():
    """Check if the request has a specific path"""
    if auth is None:
        return

    excluded_path = [
            '/api/v1/status/',
            '/api/v1/unauthorized/',
            '/api/v1/forbidden/'
            ]
    # Check if the path requires authentication
    if not auth.require_auth(request.path, excluded_path):
        return

    # Check for Authorization header
    if auth.authorization_header(request) is None:
        abort(401)  # Unauthorized if no auth header

    # Check if there is a current user
    if auth.current_user(request) is None:
        abort(403)  # Forbidden if current user is not valid


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
