#!/usr/bin/env python3
"""End-to-end integration test of the authentication service endpoints."""
import requests

BASE_URL = "http://localhost:5000"


def register_user(email: str, password: str) -> None:
    """Assert a new user can be registered exactly once."""
    response = requests.post(
        "{}/users".format(BASE_URL),
        data={"email": email, "password": password})
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "user created"}

    response = requests.post(
        "{}/users".format(BASE_URL),
        data={"email": email, "password": password})
    assert response.status_code == 400
    assert response.json() == {"message": "email already registered"}


def log_in_wrong_password(email: str, password: str) -> None:
    """Assert logging in with a wrong password is rejected with a 401."""
    response = requests.post(
        "{}/sessions".format(BASE_URL),
        data={"email": email, "password": password})
    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """Assert a valid login succeeds and return the session ID."""
    response = requests.post(
        "{}/sessions".format(BASE_URL),
        data={"email": email, "password": password})
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "logged in"}
    return response.cookies.get("session_id")


def profile_unlogged() -> None:
    """Assert accessing the profile without a session is forbidden."""
    response = requests.get("{}/profile".format(BASE_URL))
    assert response.status_code == 403


def profile_logged(session_id: str) -> None:
    """Assert a logged-in user can access their profile."""
    cookies = {"session_id": session_id}
    response = requests.get("{}/profile".format(BASE_URL), cookies=cookies)
    assert response.status_code == 200
    assert "email" in response.json()


def log_out(session_id: str) -> None:
    """Assert a logged-in user can log out and is redirected home."""
    cookies = {"session_id": session_id}
    response = requests.delete(
        "{}/sessions".format(BASE_URL), cookies=cookies)
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenue"}


def reset_password_token(email: str) -> str:
    """Assert a reset token is issued and return it."""
    response = requests.post(
        "{}/reset_password".format(BASE_URL), data={"email": email})
    assert response.status_code == 200
    assert response.json()["email"] == email
    reset_token = response.json()["reset_token"]
    assert reset_token
    return reset_token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Assert the password can be updated with a valid reset token."""
    response = requests.put(
        "{}/reset_password".format(BASE_URL),
        data={
            "email": email,
            "reset_token": reset_token,
            "new_password": new_password})
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "Password updated"}


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
