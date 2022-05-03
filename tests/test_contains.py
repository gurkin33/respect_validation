import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.ContainsException import ContainsException


@pytest.mark.parametrize('things, value', [
    [('foo', False), ['bar', 'foo']],
    [('foo', False), 'barbazFOO'],
    [('foo', False), 'barbazfoo'],
    [('foo', False), 'foobazfoO'],
    [('1', False), [2, 3, '1']],
    [('foo', ), ['fool', 'foo']],
    [('foo', ), 'barbazfoo'],
    [('foo', ), 'foobazfoo'],
    [('1', ), [2, 3, str(1)]],
    [('1', ), [2, 3, '1']],
    [(1, ), [2, 3, 1]],
])
def test_success_contains(things, value):
    assert v.contains(*things).validate(value)
    assert v.contains(*things).check(value) is None
    assert v.contains(*things).claim(value) is None


@pytest.mark.parametrize('things, value', [
    [('foo', False), ''],
    [('bat', False), ['bar', 'foo']],
    [('foo', False), 'barfaabaz'],
    [('foo', False), 'faabarbaz'],
    [('foo', True), ''],
    [('bat', True), ['BAT', 'foo']],
    [('bat', True), ['BaT', 'Batata']],
    [('foo', True), 'barfaabaz'],
    [('foo', True), 'barbazFOO'],
    [('foo', True), 'faabarbaz'],
    [(1, True), ['1', 2, 3]],
])
def test_fail_contains(things, value):
    assert v.contains(*things).validate(value) is False

    with pytest.raises(ContainsException, match="must contain the value"):
        assert v.contains(*things).check(value)
        assert v.contains(*things).claim(value)
