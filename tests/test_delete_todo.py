def test_delete_todo_success(client, get_todo):
    todo = get_todo(todo_id=1)

    response = client.delete("v1/todo/delete", params={"todo_id": todo.id})

    assert response.status_code == 200
    assert response.json() == f"Todo {todo.name} was successfully deleted"


def test_delete_todo_not_found(client):
    response = client.delete("v1/todo/delete", params={"todo_id": -1})
    assert response.status_code == 400
    assert response.json() == {"detail": "Todo not found"}
