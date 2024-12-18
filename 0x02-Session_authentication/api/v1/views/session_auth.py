#!/usr/bin/env python3
"""View for session Authentication"""


from api.v1.views import app_views
from models.user import User
from api.v1.app import auth
from flask import request, jsonify
from os import getenv


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def session_login():
    """Handles session login"""
    email = request.form.get("email")
    if not email:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get("password")
    if not password:
        return jsonify({"error": "password missing"}), 400

    users = User.search({"email": email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    response.set_cookie(getenv("SESSION_NAME"), session_id)
    return response
