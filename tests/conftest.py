import pytest

@pytest.fixture(scope="function",autouse=True)
def setup():
    print("this will print before every function")
    yield
    print("this will print after every function")
