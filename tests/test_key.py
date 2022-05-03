import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions import ValidationException


@pytest.mark.parametrize('key_rule,value', [
    [('foo', v.equals('bar')), {'foo': 'bar', 'foo1': None}],
    [('foo1', v.noneType()), {'foo': 'bar', 'foo1': None}]
])
def test_success_key(key_rule, value):
    assert v.key(*key_rule).validate(value)
    assert v.key(*key_rule).check(value) is None
    assert v.key(*key_rule).claim(value) is None


@pytest.mark.parametrize('key_rule,value', [
    [('foo', v.equals('bar')), {'foo': None, 'foo1': None}],
    [('foo1', v.noneType()), {'foo': 'bar', 'foo1': 123123}],
    [('foo', v.equals('bar')), {'foo1': None}],
    [('foo1', v.noneType()), {}],
    [('foo1', v.noneType()), None],
])
def test_fail_key(key_rule, value):
    assert v.key(*key_rule).validate(value) is False

    with pytest.raises(ValidationException, match=r'(foo.* must be present|foo1 must be None type|foo must be equal to bar)'):
        assert v.key(*key_rule).check(value)
        assert v.key(*key_rule).claim(value)
