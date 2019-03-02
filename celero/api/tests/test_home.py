import pytest


@pytest.fixture
def resp(client, db):
    resp = client.get('/api/v1')
    return resp


def test_status_code(resp):
    assert resp.status_code == 200
