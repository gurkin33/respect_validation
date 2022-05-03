import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.DigitException import DigitException


@pytest.mark.parametrize('more_char, value', [
    [None, 165],
    [None, '01650'],
    ['-', '16-50'],
    ['.-', '16-5.0'],
    ['!@#$%^&*(){}', '!@#$%^&*(){}'],
    [('.', '-'), '012.071.070-69'],
    [None, '01']
])
def test_success_digit(more_char, value):
    if more_char:
        assert v.digit(*more_char).validate(value)
        assert v.digit(*more_char).check(value) is None
        assert v.digit(*more_char).claim(value) is None
    else:
        assert v.digit().validate(value)
        assert v.digit().check(value) is None
        assert v.digit().claim(value) is None


@pytest.mark.parametrize('value', [
    '1.0',
    True,
    '16 50',
    '1\t1',
    '1\n1',
    None,
    '16-50',
    'a',
    'a1',
    -12,
    '-12',
    -1.1,
    '-1.1',
    False
])
def test_fail_digit(value):
    assert v.digit().validate(value) is False
    with pytest.raises(DigitException, match="must contain only digits \\(0-9\\)"):
        assert v.digit().check(value)
        assert v.digit().claim(value)
