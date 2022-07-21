def test_create_user_success(client, get_user_by_id):
    user_to_create = {"username": "a123-ha_", "password": "foobar"}

    response = client.post("v1/user/create", json=user_to_create)

    created_user = get_user_by_id(response.json()["id"])
    assert response.status_code == 201
    assert response.json() == created_user


def test_create_user_already_exists(client):
    user_to_create = {"username": "a123-ha_", "password": "foobar"}

    response = client.post("v1/user/create", json=user_to_create)
    assert response.status_code == 400
    assert response.json() == {"detail": "User already exists"}


def test_create_user_invalid_username(client):
    user_to_create = {"username": "a[].x weion201\}", "password": "foobar"}

    response = client.post("v1/user/create", json=user_to_create)

    assert response.status_code == 400
    assert response.json() == {"detail": "Username may contain invalid characters"}
