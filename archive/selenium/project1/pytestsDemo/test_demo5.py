#pytest files should start with 'test_' or end with 'test_'
#pytest methods should start with 'test_'

import pytest




@pytest.mark.usefixtures("setup2")
class TestUsingFixtures:
    def test_01(self):
        varA = 1
        varB = 1
        assert varA == varB

    def test_02(self):
        varA = 1
        varB = 1
        assert varA == varB  

    def test_03(self):
        varA = 1
        varB = 1
        assert varA == varB

    def test_04(self):
        varA = 1
        varB = 1
        assert varA == varB
