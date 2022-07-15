import pytest
from config import SESSION, APP_URL, ADMIN_USER, ADMIN_PASSWORD, LOG

@pytest.fixture(scope='session')
def login_as_admin():
    LOG.info("login_as_admin()")
    payload = {"username": ADMIN_USER, "password": ADMIN_PASSWORD}
    LOG.debug(f"Login payload: {payload}")
    response = SESSION.post(f"{APP_URL}/auth/login", data=payload)
    assert response.ok
    access_token = response.json()["access_token"]
    yield access_token