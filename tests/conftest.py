import pytest
from praktikum.bun import Bun

@pytest.fixture
def create_bun():
    bun = Bun('Сырная булочка', 1.15)
    return bun
