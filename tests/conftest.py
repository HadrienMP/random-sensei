import pytest
import application


@pytest.fixture
def app():
    return application.app

