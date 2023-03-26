
import pytest

# @pytest.fixture() # <- this would make the setup being executed at every method
@pytest.fixture(scope="class")
def setup2():
    print("setup2() - this will be executed first")
    yield
    print("setup2() - this will be executed last")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["FirstName","LastName","last.first@domain.com"]