import pytest

from api import app

@pytest.fixture
def api_context():
    return ("Marcin")

def test_hello():
    resp = app.hello()

    assert resp == "Hello!"

def test_hello_you(api_context):
    resp = app.hello_you(api_context)

    assert resp == {'message': 'hello Marcin'}