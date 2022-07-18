from app import app # Flask instance of the API
import json

def test_index_route():
    response = app.test_client().get('/')
    res = json.loads(response.data.decode('utf-8'))
    assert response.status_code == 200
    assert res == {"hello": "world"}