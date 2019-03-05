from celero.api.apps import ApiConfig


def test_home():
    assert ApiConfig.name == 'api'
