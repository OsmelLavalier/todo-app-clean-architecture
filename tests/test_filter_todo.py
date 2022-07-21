def test_filter_by_state_success(client):
    response = client.get("v1/todo/filter", params={"state": "New"})

    assert response.status_code == 200

    assert response.json()[0]["state"] == "New"


def test_filter_by_state_in_progress(client):
    todo_to_create = {"name": "Test Todo 2", "data": "Finish homework"}

    response = client.post(
        "v1/todo/create",
        json=todo_to_create,
        params={"user_id": 1, "state": "In Progress"},
    )
    assert response.status_code == 201

    response2 = client.get("v1/todo/filter", params={"state": "In Progress"})
    assert response2.status_code == 200
    assert response2.json()[0]["state"] == "In Progress"


def test_filter_by_state_missing_state(client):
    response = client.get("v1/todo/get", params={"state": ""})
    assert response.status_code == 422
    response.json()[
        "detail"
    ] == "[{'loc': ['query', 'todo_id'], 'msg': 'field required', 'type': 'value_error.missing'}]"
