# test_hello_add.py
from user import app
from flask import json

def test_add():
    response = app.test_client().post(
        '/users',
        data=json.dumps({'a': 1, 'b': 2}),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['sum'] == 3
