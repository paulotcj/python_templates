#pytest files should start with 'test_' or end with 'test_'
#pytest methods should start with 'test_'

import pytest

def test_Tests_03():
    msg = "Hello"

    expected = "Hello3"
    assert msg == expected , f"Custom Message - Test failed, expected:{expected} but received:{msg}"

def test_Tests_04():
    msg = "Hello"

    expected = "Hello"
    assert msg == expected , f"Custom Message - Test failed, expected:{expected} but received:{msg}"


def test_Tests_05_SomeSpecificKeyWord():
    msg = "Hello"

    expected = "Hello"
    assert msg == expected , f"Custom Message - Test failed, expected:{expected} but received:{msg}"

@pytest.mark.SpecificMark01
def test_Tests_06_SomeSpecificKeyWord():
    msg = "Hello"

    expected = "Hello"
    assert msg == expected , f"Custom Message - Test failed, expected:{expected} but received:{msg}"


@pytest.mark.skip
def test_Tests_07():
    msg = "Hello"

    expected = "Hello----------------"
    assert msg == expected , f"Custom Message - Test failed, expected:{expected} but received:{msg}"    



