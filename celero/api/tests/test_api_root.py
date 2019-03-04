import pytest

"""
Executa testes referentes à página inicial da API - (API Root)
"""


@pytest.fixture
def resp(client, db):
    resp = client.get('/')
    return resp


def test_status_code(resp):
    assert resp.status_code == 200
