"""Testing Sample Calculation """
from flask import url_for
from flask_login import current_user

from application.database import User


def test_main_menu_authenticated(client, login):
    response = client.get("/dashboard")
    assert response.status_code == 200
    assert b"Logout" in response.data
    assert b"My Profile" in response.data
