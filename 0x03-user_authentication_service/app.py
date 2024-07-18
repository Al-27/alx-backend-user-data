#!/usr/bin/env python3
"""APP
"""
from flask import Flask, jsonify, request, session, abort
from auth import Auth
import os


AUTH = Auth()
app = Flask(__name__)
app.secret_key = str(os.urandom(24))

@app.route("/")
def root():
    """ROUTE
    """
    return jsonify({"message": "Bienvenue"})

@app.route('/users',methods=['POST'])
def users():
    """ROUTE
    """
    email = request.form["email" ]
    pwd = request.form["password"]
    try:
        user = AUTH.register_user(email, pwd)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    
    return jsonify({"email": email, "message": "user created"})

@app.route('/sessions', methods=["POST"])
def login():
    """ROUTE
    """
    email = request.form['email']
    pwd = request.form['password']

    if AUTH.valid_login(email,pwd):
        session['session_id'] = AUTH.create_session(email)
        return jsonify({"email": email, "message": "logged in"})
    
    return abort(401) 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")