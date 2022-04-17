import pytest


def test_list_all(client):
    res = client.get('/api/byCoders/list/all')
    assert res.status_code == 200
    json_data = res.get_json()
    assert len(json_data) > 0


@pytest.mark.parametrize("store_id, status_error", [
    (1, 200),
    (2, 200),
    (3, 200),
    (4, 200),
    (5, 200),
    (6, 400),
    (70000, 400)
])
def test_list_store(client, store_id, status_error):
    res = client.get(f'/api/byCoders/list/{store_id}')
    assert res.status_code == status_error
    json_data = res.get_json()
    if status_error == 400:
        assert json_data.get('message')
    else:
        assert len(json_data) > 0
