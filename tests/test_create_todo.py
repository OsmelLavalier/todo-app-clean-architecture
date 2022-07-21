def test_create_todo_success(client, get_user_by_username):
    todo_owner = {"username": "Foo", "password": "Bar"}
    todo_to_create = {"name": "Test Todo", "data": "Finish homework"}

    response = client.post("v1/user/create", json=todo_owner)

    assert response.status_code == 201

    response2 = client.post(
        "v1/todo/create",
        json=todo_to_create,
        params={"user_id": response.json()["id"], "state": "New"},
    )
    created_owner = get_user_by_username(username=todo_owner["username"])
    assert response2.status_code == 201
    assert len(created_owner.todos) == 1

    for k, v in created_owner.todos[0].dict().items():
        if k != "created_at":
            assert response2.json()[k] == v


def test_create_todo_no_owner(client):
    todo_to_create = {"name": "Test Todo", "data": "Finish homework"}

    response = client.post(
        "v1/todo/create",
        json=todo_to_create,
        params={"user_id": -1, "state": "New"},
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "User not found"}


def test_create_todo_with_unknown_state(client):
    response = client.post(
        "v1/todo/create",
        json={"name": "Test Todo", "data": "Finish homework"},
        params={"user_id": 1, "state": "Unknown State"},
    )
    assert response.status_code == 422
    assert response.json()["detail"] == [
        {
            "ctx": {"enum_values": ["New", "Active", "In Progress", "Done"]},
            "loc": ["query", "state"],
            "msg": "value is not a valid enumeration member; permitted: 'New', 'Active', "
            "'In Progress', 'Done'",
            "type": "type_error.enum",
        }
    ]
