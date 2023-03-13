
import pytest

# @pytest.fixture() # <- this would make the setup being executed at every method
@pytest.fixture(scope="class")
def setup2():
    print("setup2() - this will be executed first")
    yield
    print("setup2() - this will be executed last")