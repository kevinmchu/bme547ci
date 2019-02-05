import pytest
from tachycardia import is_tachycardic


@pytest.mark.parametrize("test_str, expected", [('tachycardic', True),
                                                ('TACHYCARDIC', True),
                                                ('TaChYcArDiC', True),
                                                ('  tachycardic', True),
                                                ('tachycardic  ', True),
                                                ('  tachycardic  ', True),
                                                ('.tachycardic', True),
                                                ('tachycardic.', True),
                                                (';tachycardic;', True),
                                                ('..tachycardic', True),
                                                ('hellotachycardic', True),
                                                ('1234tachycardic', True),
                                                ('!@#$tachycardic', True),
                                                ('\ntachycardic\n', True),
                                                ('tachycardia', False),
                                                ('tachycard1c', False),
                                                ('hello', False),
                                                ('HELLO', False),
                                                ('HeLlO', False),
                                                ('', False),
                                                ('     ', False),
                                                ('tachy.cardic', False),
                                                ('tachy cardic', False)])
def test_is_tachycardic(test_str, expected):

    answer = is_tachycardic(test_str)
    assert answer == expected
