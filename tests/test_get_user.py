def test_get_user_success(client, get_user_by_username):
    response = client.get("v1/user/get", params={"username": "a123-ha_"})
    db_user = get_user_by_username(username="a123-ha_")

    assert response.status_code == 200
    for k, v in db_user.dict().items():
        if k != "todos":
            assert response.json()[k] == v


def test_get_user_does_not_exists(client):
    response = client.get("v1/user/get", params={"username": ""})
    assert response.status_code == 400
    assert response.json() == {"detail": "User not found"}
