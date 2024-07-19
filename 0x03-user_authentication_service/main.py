#!/usr/bin/env python3
"""Main
"""
import requests
from flask import jsonify


def register_user(email: str, password: str) -> None:
    """func
    """
    resp = requests.post(
        "0.0.0.0:5000/users",
        data={
            'email': email,
            'password': password})
    assert (resp.status_code == 200)
    assert (resp.text == jsonify({"email": email, "message": "user created"}))


def log_in_wrong_password(email: str, password: str) -> None:
    """func
    """
    resp = requests.post(
        "0.0.0.0:5000/sessions",
        data={
            'email': email,
            'password': password})
    assert (resp.status_code == 401)


def log_in(email: str, password: str) -> str:
    """func
    """
    resp = requests.post(
        "0.0.0.0:5000/sessions",
        data={
            'email': email,
            'password': password})
    assert (resp.status_code == 200)
    assert (resp.text == jsonify({"email": email, "message": "logged in"}))


def profile_unlogged() -> None:
    """func
    """
    pass


def profile_logged(session_id: str) -> None:
    """func
    """
    pass


def log_out(session_id: str) -> None:
    """func
    """
    resp = requests.delete(
        "0.0.0.0:5000/sessions",
        data={
            'session_id': session_id})
    assert (resp.status_code == 302)


def reset_password_token(email: str) -> str:
    """func
    """
    resp = requests.post("0.0.0.0:5000/reset_password", data={'email': email})
    assert (resp.status_code == 200)


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """func
    """
    resp = requests.put(
        "0.0.0.0:5000/reset_password",
        data={
            'email': email,
            "reset_token": reset_token,
            "new_password": new_password})
    assert (resp.status_code == 200)
    assert (resp.text == jsonify(
        {"email": email, "reset_token": "Password updated"}))


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
