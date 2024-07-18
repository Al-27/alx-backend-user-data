#!/usr/bin/env python3
"""APP
"""
from flask import Flask, jsonify, request, session, abort, redirect, url_for
from auth import Auth
import os


AUTH = Auth()
app = Flask(__name__)
app.secret_key = str(os.urandom(24))

@app.route("/")
def index():
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
    
    abort(401) 

@app.route("/sessions", methods=['DELETE'])
def logout():
    """logout
    """
    if "session_id" in request.cookies:
        sess_id = request.cookies["session_id"]
        user = AUTH.get_user_from_session_id(sess_id)
        if user :
            session.pop("session_id")
            AUTH.destroy_session(user.id)
            return redirect(url_for("index"))
    abort(403)
    
@app.route('/profile')
def profile():
    """func
    """
    ss_id = request.cookies['session_id']
    user = AUTH.get_user_from_session_id(ss_id)
    if user:
        return jsonify({"email": user.email})
    
    abort(403)

@app.route('/reset_password', methods=["POST"])
def get_reset_password_token():
    """func
    """
    email = request.form['email']
    try:
        res_tok = AUTH.get_reset_password_token(email)
    except:
        abort(403)
    
    return jsonify({"email": email, "reset_token": res_tok})

@app.route('/reset_password', methods=["PUT"])
def update_password ():
    """func
    """
    email = request.form['email']
    res_tok = request.form['reset_token']
    try:
        AUTH.update_password(res_tok, request.form['new_password'])
    except:
        abort(403)
    
    return jsonify({"email": email, "reset_token": "Password updated"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")