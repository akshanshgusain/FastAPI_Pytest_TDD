import pytest
from starlette.testclient import TestClient

from app import main


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(main.app)
    yield client  # testing happens here