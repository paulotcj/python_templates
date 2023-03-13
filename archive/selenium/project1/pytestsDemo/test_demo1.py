#pytest files should start with 'test_' or end with 'test_'
#pytest methods should start with 'test_'

import pytest

def test_firstProgram():
    print("Hello world")

    assert 1==1

def test_Tests_01():
    msg = "Hello"

    expected = "Hello"
    assert msg == expected , f"Test failed, expected:{expected} but received:{msg}"

@pytest.mark.SpecificMark01
def test_Tests_02():
    msg = "Hello"

    expected = "Hello World"
    assert msg == expected , f"Custom Message - Test failed, expected:{expected} but received:{msg}"


def test_Tests_07_SomeSpecificKeyWord():
    msg = "Hello"

    expected = "Hello"
    assert msg == expected , f"Custom Message - Test failed, expected:{expected} but received:{msg}"


