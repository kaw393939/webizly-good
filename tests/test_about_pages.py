from faker import Faker

from application.database import User, db


def test_about_route(client):
    response = client.get("/about")
    assert response.status_code == 401
    assert b"About" in response.data
