import pytest as pytest

from data_structures_py.linked_list.stack_queue_brackets import validate_brackets as mbv


def test_one():
    actual = mbv('1')
    expected = True
    assert actual == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ('{}', True),
        ('{}(){}', True),
        ('()[[Extra Characters]]', True),
        ('(){}[[]]', True),
        ('{}{Code}[Fellows](())', True),
        ('[({}]', False),
        ('(](', False),
        ('{(})}', False),
        ('{', False),
        (')', False),
        ('[}', False)
    ]
)
def test_bracket_validation(test_input, expected):
    actual = mbv(test_input)
    assert actual == expected


def testtesttest():
    actual = mbv('{}')
    expected = True
    assert actual == expected
