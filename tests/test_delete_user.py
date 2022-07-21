def test_delete_user_success(client, get_user_by_username, delete_user):
    user = get_user_by_username(username="a123-ha_")

    response = client.delete("v1/user/delete", params={"user_id": user.id})

    assert response.status_code == 200
    assert response.json() == f"User {user.username} was successfully deleted"


def test_deleted_user_not_exist(client):
    response = client.delete("v1/user/delete", params={"user_id": -1})

    assert response.status_code == 400
    assert response.json() == {"detail": "User not found"}
