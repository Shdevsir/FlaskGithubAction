from app import app
from mock import patch
from pytest import fixture
import os
import json


@fixture
def env_var():
    with patch.dict(os.environ, {"QUESTION": "How are you?",
                                 "ANSWER": "Fine, thanks"}):
        yield


def test_hello_route():
    response = app.test_client().get('/')
    res = json.loads(response.data.decode('utf-8'))
    assert response.status_code == 200
    assert res == {"hello": "world"}


def test_secret_route(env_var):
    response = app.test_client().get('/secret')
    res = json.loads(response.data.decode('utf-8'))
    assert response.status_code == 200
    assert res == {"How are you?": "Fine, thanks"}
