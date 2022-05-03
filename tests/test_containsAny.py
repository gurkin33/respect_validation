import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.ContainsAnyException import ContainsAnyException


@pytest.mark.parametrize('things, value', [
    [(['Something', 'Else'],), 'Something else'],
    [(['Something', 'Else'], False), 'something else'],
    [([True, ],), [1, 2, 3]],
    [([[True], True],), [True]],
    [(['1', ],), ['1', 2, 3]],
    [([[1], True],), [1, 2, 3]],
    [(['word', '@', '/'],), 'lorem ipsum @ word'],
    [(['foo', 'qux'],), 'foobarbaz'],
    [(['foo', True],), ['foo', 'bar']],
])
def test_success_containsAny(things, value):
    assert v.containsAny(*things).validate(value)
    assert v.containsAny(*things).check(value) is None
    assert v.containsAny(*things).claim(value) is None


@pytest.mark.parametrize('things, value', [
    [['foo'], ['bar', 'baz']],
    [['foo', 'bar'], ['baz', 'qux']],
    [['foo', 'bar'], ['FOO', 'BAR']],
    [['foo', True], ['bar', 'baz']],
    [['foo', 'bar', True], ['FOO', 'BAR']],
    [['whatever'], ''],
    [[''], 'whatever'],
    [[False], ''],
    [['foo', 'qux'], 'barbaz'],
    [[1, 2, 3, True], ['1', '2', '3']],
    [['word', '@', '/'], 'lorem ipsum'],
])
def test_fail_containsAny(things, value):
    assert v.containsAny(things).validate(value) is False

    with pytest.raises(ContainsAnyException, match="must contain at least one of the values"):
        assert v.containsAny(things).check(value)
        assert v.containsAny(things).claim(value)
