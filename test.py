from app import app

def test_hello_world():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert response.get_data(as_text=True) == 'This is Jenkins file Pipeline first API call!'
        