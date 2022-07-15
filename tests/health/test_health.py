import requests

def test_health():
    response = requests.get("http://127.0.0.1:8080/health")
    assert response.ok