import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.PositiveException import PositiveException


@pytest.mark.parametrize('value', [
    16,
    '165',
    123456,
    1e10,
])
def test_success_positive(value):
    assert v.positive().validate(value)
    assert v.positive().check(value) is None
    assert v.positive().claim(value) is None


@pytest.mark.parametrize('value', [
    '',
    [],
    object(),
    None,
    'a',
    ' ',
    'Foo',
    '-1.44',
    -1e-5,
    0,
    -0,
    -10,
])
def test_fail_positive(value):
    assert v.positive().validate(value) is False

    with pytest.raises(PositiveException, match=r' must be positive'):
        assert v.positive().check(value)
        assert v.positive().claim(value)
