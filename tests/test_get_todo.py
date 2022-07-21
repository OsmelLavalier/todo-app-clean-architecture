def test_get_todo_success(client, get_todo):
    response = client.get("v1/todo/get", params={"todo_id": 1})

    assert response.status_code == 200

    db_todo = get_todo(todo_id=response.json()["id"])

    for k, v in db_todo.dict().items():
        if k != "created_at":
            assert response.json()[k] == v


def test_get_todo_not_found(client):
    respone = client.get("v1/todo/get", params={"todo_id": -1})

    assert respone.status_code == 400
    assert respone.json() == {"detail": "Todo not found"}
