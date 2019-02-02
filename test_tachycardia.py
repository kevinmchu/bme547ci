import pytest
from tachycardia import is_tachycardic


@pytest.mark.parametrize("test_str, expected", [('tachycardic', True),
                                                ('TACHYCARDIC', True),
                                                ('TaChYcArDiC', True),
                                                ('  tachycardic', True),
                                                ('tachycardic  ', True),
                                                ('  tachycardic  ', True),
                                                ('hello', False),
                                                ('HELLO', False),
                                                ('HeLlO', False)])
def test_is_tachycardic(test_str, expected):

    answer = is_tachycardic(test_str)
    assert answer == expected
