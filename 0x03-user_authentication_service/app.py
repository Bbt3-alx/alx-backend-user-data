#!/usr/bin/env python3
"""Basic flask app"""


from flask import Flask, jsonify, request
from auth import Auth
from db import DB


AUTH = Auth()

app = Flask(__name__)


@app.route("/")
def home():
    """Return JSON payload of the form"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["GET", "POST"])
def register_user():
    """Register a user"""
    if request.method == "POST":
        email = request.form.get("emil")
        password = request.form.get("password")
        try:
            new_user = AUTH.register_user(email, password)
            return new_user
        except ValueError:
            return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
