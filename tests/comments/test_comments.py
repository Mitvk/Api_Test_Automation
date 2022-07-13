import pytest
import requests
from lib_.utils import build_request_headers
from lib_.comments import Comments
from config import APP_URL, LOG

def test_get_all_comments(login_as_admin):
    # request_header = build_request_headers(login_as_admin)
    # response = requests.get('http://127.0.0.1:8080/comments/', headers=request_header)
    # assert response.ok
    LOG.info('test_get_all_comments')
    response = Comments().get_all_comments(APP_URL, login_as_admin)
    LOG.debug(response.json())
    assert response.ok


def test_cud_comment(login_as_admin):
    LOG.info('test_cud_comment')
    LOG.info('Creating comment')
    response = Comments().create_comment(APP_URL, login_as_admin, "first post")
    assert response.ok
    response_data = response.json()
    comment_id = response_data['id']
    LOG.info(response_data)
    assert response_data['comment_text'] == "first post"

    LOG.info(f'Updating the comment with comment id : {comment_id}')
    response = Comments().update_comment(APP_URL, login_as_admin, comment_id, message='Updated to second one', likes=700)
    assert response.ok
    response_data = response.json()
    LOG.info(f"Response payload : {response_data}")
    assert response_data['comment_text'] == "Updated to second one"
    assert response_data["likes"] == 700
