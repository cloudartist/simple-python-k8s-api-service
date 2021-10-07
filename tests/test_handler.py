import pytest

from app import api

@pytest.fixture
def api_context():
    return ("Marcin")

def test_hello():
    resp = api.hello()

    assert resp == {'message': 'Hello!'}

def test_hello_you(api_context):
    resp = api.hello_you(api_context)

    assert resp == {'message': 'hello Marcin'}
