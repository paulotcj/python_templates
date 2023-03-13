#pytest files should start with 'test_' or end with 'test_'
#pytest methods should start with 'test_'

import pytest




@pytest.fixture()
def setup():
    print("setup() - this will be executed first")
    yield
    print("setup() - this will be executed last")

def test_fixtureDemo(setup):
    print("steps being executed in the test_fixtureDemo")