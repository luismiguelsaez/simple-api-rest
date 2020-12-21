from requests import get,put,post,delete,patch
from os import environ

def test_get_base_status_code_equals_200():
     response = get(environ.get('ENDPOINT'))
     assert response.status_code == 200

def test_get_db_test_equals_200():
     response = get(environ.get('ENDPOINT') + "/db/test")
     assert response.status_code == 200

def test_get_db_database_collection_200():
     response = get(environ.get('ENDPOINT') + "/db/testdb/testcoll")
     assert response.status_code == 200

def test_put_db_database_collection_200():
     response = put(environ.get('ENDPOINT') + "/db/testdb/testcoll")
     assert response.status_code == 200

def test_post_db_database_collection_200():
     response = post(environ.get('ENDPOINT') + "/db/testdb/testcoll")
     assert response.status_code == 200

def test_delete_db_database_collection_200():
     response = delete(environ.get('ENDPOINT') + "/db/testdb/testcoll")
     assert response.status_code == 200

def test_patch_db_database_collection_404():
     response = patch(environ.get('ENDPOINT') + "/db/testdb/testcoll")
     assert response.status_code == 404