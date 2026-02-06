import requests

def test_ping():
    r = requests.get("http://localhost:8080/api/ping")
    assert r.status_code == 200
    assert r.json() == {"response": "pong"}
