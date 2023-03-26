import pytest

@pytest.mark.usefixtures("dataLoad")
class TestUsingFixtures_Example2:
    def test_01(self, dataLoad):
        print(dataLoad)
