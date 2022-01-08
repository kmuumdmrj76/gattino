import pytest
from gattino import Gattino


@pytest.fixture()
def gattino_app():
    return Gattino()
