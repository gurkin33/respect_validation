import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions import ComponentException
from respect_validation.Exceptions.CallbackException import CallbackException


def compare(thing: int):
    return thing > 10


def test_success_callback():
    assert v.callback(compare).validate(20)
    assert v.callback(compare).check(20) is None
    assert v.callback(compare).claim(20) is None


def test_fail_callback():
    assert v.callback(compare).validate(5) is False

    with pytest.raises(CallbackException, match='"5" must be valid'):
        assert v.callback(compare).check(5)
        assert v.callback(compare).claim(5)


@pytest.mark.parametrize('value', [
    '',
    'foo',
    123123,
    object(),
    [],
    1,
    0,
    None,
])
def test_fail_callback2(value):

    with pytest.raises(ComponentException, match='Callback must be callable'):
        assert v.callback(value).validate(value)
        assert v.callback(value).check(value)
        assert v.callback(value).claim(value)
