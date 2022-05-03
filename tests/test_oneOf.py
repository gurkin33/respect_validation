import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.OneOfException import OneOfException


@pytest.mark.parametrize('value', [
    -5,
    'abc'
])
def test_success_oneOf(value):
    assert v.oneOf(v.number(), v.stringType()).validate(value)
    assert v.oneOf(v.number(), v.stringType()).check(value) is None
    assert v.oneOf(v.number(), v.stringType()).claim(value) is None


@pytest.mark.parametrize('value', [
    '-1',
    '5'
])
def test_fail_oneOf(value):
    assert v.oneOf(v.number(), v.stringType()).validate(value) is False

    with pytest.raises(OneOfException, match=r'Only one of these rules must pass for '):
        assert v.oneOf(v.number(), v.stringType()).check(value)
        assert v.oneOf(v.number(), v.stringType()).claim(value)
