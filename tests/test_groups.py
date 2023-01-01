"""Testing User Profile """
from flask_login import current_user

from application.database import User, db, Profile, Group


def test_group_model(app, create_5_users):
    with app.app_context():
        assert Group.record_count() == 0
        group = Group("Group One")
        group.save()
        assert Group.record_count() == 1


def test_new_group_post_controller(app, client, login):
    with client:
        response = client.post("/groups/new", data={
            "title": "My Group",
        }, follow_redirects=True)
        assert response.status_code == 200
    with app.app_context():
        assert Group.record_count() == 1


def test_group_model_join_membership(app, create_5_users, faker):
    with app.app_context():
        groups = []
        assert Group.record_count() == 0
        for _ in range(100):
            group = Group(faker.catch_phrase())
            groups.append(group)
        Group.add_all(groups)

        assert Group.record_count() == 100
        for _ in range(10):
            user = User.get_random_record()
            for _ in range(5):
                user.groups.append(Group.get_random_record())
                user.save()
