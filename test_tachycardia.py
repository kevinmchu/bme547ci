from tachycardia import is_tachycardic


def test_1():

    answer = is_tachycardic("tachycardic")
    expected = True

    assert answer == expected


def test_2():

    answer = is_tachycardic("abcdefg")
    expected = False

    assert answer == expected
