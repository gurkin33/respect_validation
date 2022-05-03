import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.NoWhitespaceException import NoWhitespaceException


@pytest.mark.parametrize('value', [
    '',
    None,
    0,
    'wpoiur',
    'Foo',
    []
])
def test_success_noWhitespace(value):
    assert v.noWhitespace().validate(value)
    assert v.noWhitespace().check(value) is None
    assert v.noWhitespace().claim(value) is None


@pytest.mark.parametrize('value', [
    [1, 2],
    object(),
    {'name': '123123'},
    ' a',
    ' ',
])
def test_fail_noWhitespace(value):
    assert v.noWhitespace().validate(value) is False

    with pytest.raises(NoWhitespaceException, match=r' must not contain whitespace'):
        assert v.noWhitespace().check(value)
        assert v.noWhitespace().claim(value)
