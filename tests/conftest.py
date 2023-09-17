import os
import pytest
from fastapi.testclient import TestClient


@pytest.fixture(scope="session")
def monkey_patch_session():
    from _pytest.monkeypatch import MonkeyPatch

    m = MonkeyPatch()
    yield m
    m.undo()


@pytest.fixture(scope="session")
def mock_env(monkey_patch_session):

    monkey_patch_session.setenv("PYTHONPATH", os.getcwd())
    monkey_patch_session.setenv("ENVIRONMENT", "local")
    monkey_patch_session.setenv("FASTAPI_SERVICE_NAME", "Enterpret")
    monkey_patch_session.setenv("FASTAPI_PORT_MODEL_HOSTER", "8080")
    monkey_patch_session.setenv("FASTAPI_PORT_MODEL_MANAGEMENT", "8081")
    monkey_patch_session.setenv("FASTAPI_PORT_MODEL_EXECUTOR", "8082")
    monkey_patch_session.setenv("FASTAPI_HOST", "0.0.0.0")
    monkey_patch_session.setenv("MODEL_MANAGEMENT_URL", "localhost:8081")
    monkey_patch_session.setenv("MODEL_HOSTER_URL", "localhost:8080")
    monkey_patch_session.setenv("FASTAPI_HOST", "0.0.0.0")


@pytest.fixture(scope="module")
def text_client_model_hoster(mock_env):
    """
    Creates a test client
    :param mock_env:
    :return:
    """
    from model_hoster.app import app
    test_client = TestClient(app)
    return test_client


@pytest.fixture(scope="module")
def text_client_model_management(mock_env):
    """
    Creates a test client
    :param mock_env:
    :return:
    """
    from model_management.app import app
    test_client = TestClient(app)
    return test_client


@pytest.fixture(scope="module")
def text_client_model_executor(mock_env):
    """
    Creates a test client
    :param mock_env:
    :return:
    """
    from model_executor.app import app
    test_client = TestClient(app)
    return test_client
