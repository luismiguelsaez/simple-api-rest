import requests

def test_base_get():
     response = requests.get("http://localhost:8080")
     assert response.status_code == 200
