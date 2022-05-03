import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.PunctException import PunctException


@pytest.mark.parametrize('value', [
    '.',
    ',;:',
    '-@#$*',
    '()[]{}',
])
def test_success_punct(value):
    assert v.punct().validate(value)
    assert v.punct().check(value) is None
    assert v.punct().claim(value) is None


@pytest.mark.parametrize('value', [
    '',
    '16-50',
    'a',
    ' ',
    'Foo',
    '12.1',
    '-12',
    -12,
    '( )_{}',
])
def test_fail_punct(value):
    assert v.punct().validate(value) is False

    with pytest.raises(PunctException, match=r' must contain only punctuation characters'):
        assert v.punct().check(value)
        assert v.punct().claim(value)
