import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions import ValidationException


def repeat_it_please(thing):
    return thing


@pytest.mark.parametrize('value', [
    '612890053',
    '087880532',
    '386625918',
    '601608021',
    '254650703',
    '478063441',
    '478063441',
    '187368429',
    '541777348',
    '254283883',
])
def test_success_call(value):
    assert v.call(repeat_it_please, v.stringType().number().length(3, 10)).validate(value)
    assert v.call(repeat_it_please, v.stringType().number().length(3, 10)).check(value) is None
    assert v.call(repeat_it_please, v.stringType().number().length(3, 10)).claim(value) is None


@pytest.mark.parametrize('value', [
    123123,
    object(),
    [],
    1,
    0,
    None,
])
def test_fail_call(value):
    assert v.call(repeat_it_please, v.stringType().number().length(3, 10)).validate(value) is False

    with pytest.raises(ValidationException, match='"Callable function or method" must be valid'):
        assert v.call(value, v.stringType().number().length(3, 10)).check(value) is None

    with pytest.raises(ValidationException):
        assert v.call(repeat_it_please, v.stringType().number().length(3, 10)).check(value)
        assert v.call(repeat_it_please, v.stringType().number().length(3, 10)).claim(value)


@pytest.mark.parametrize('value', [
    '',
    'foo',
])
def test_fail_call2(value):
    assert v.call(repeat_it_please, v.stringType().number().length(3, 10)).validate(value) is False

    with pytest.raises(ValidationException, match='Callable function or method must be valid when executed with'):
        assert v.call(value, v.stringType().number().length(3, 10)).check(value) is None

    with pytest.raises(ValidationException):
        assert v.call(repeat_it_please, v.stringType().number().length(3, 10)).check(value)
        assert v.call(repeat_it_please, v.stringType().number().length(3, 10)).claim(value)
