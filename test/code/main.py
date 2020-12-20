from requests import get,post
from os import environ

def test_get_base_status_code_equals_200():
     response = get(environ.get('ENDPOINT'))
     assert response.status_code == 200

def test_get_db_test_equals_200():
     response = get(environ.get('ENDPOINT') + "/db/test")
     assert response.status_code == 200