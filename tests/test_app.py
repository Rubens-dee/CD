from conftest import client


def test_should_status_code_ok(client):
    response = client.get('/')
    assert response.status_code == 200
    response = client.get('/form')
    assert response.status_code == 200
    response = client.post('/submit', data={"name": "Ruben1"})
    assert response.status_code == 200
