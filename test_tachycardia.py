import pytest
from tachycardia import is_tachycardic


@pytest.mark.parametrize("test_str, expected", [('TACHYCARDIC', True),
                                                ('HELLO', False)])
def test_is_tachycardic(test_str, expected):

    answer = is_tachycardic(test_str)
    assert answer == expected


def test_1():

    answer = is_tachycardic("tachycardic")
    expected = True

    assert answer == expected


def test_2():

    answer = is_tachycardic("abcdefg")
    expected = False

    assert answer == expected
