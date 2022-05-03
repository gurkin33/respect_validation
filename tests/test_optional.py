import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.OptionalException import OptionalException


@pytest.mark.parametrize('value', [
    None,
    '',
])
def test_success_optional(value):
    assert v.optional(v.phone()).validate(value)
    assert v.optional(v.phone()).check(value) is None
    assert v.optional(v.phone()).claim(value) is None


@pytest.mark.parametrize('value', [
    1,
    [],
    ' ',
    0,
    '0',
    0,
    '0.0',
    False,
    [''],
    [' '],
    [0],
    ['0'],
    [False],
    [[''], [0]],
    object(),
])
def test_fail_optional(value):
    assert v.Not(v.optional(v.Not(v.NoneType()))).validate(value) is False

    with pytest.raises(OptionalException, match=r' must not be optional'):
        assert v.Not(v.optional(v.Not(v.NoneType()))).check(value)
        assert v.Not(v.optional(v.Not(v.NoneType()))).claim(value)
