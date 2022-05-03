import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.SpaceException import SpaceException


@pytest.mark.parametrize('value', [
    "\n",
    ' ',
    '    ',
    "\t",
    '  ',
])
def test_success_space(value):
    assert v.space().validate(value)
    assert v.space().check(value) is None
    assert v.space().claim(value) is None


@pytest.mark.parametrize('value', [
    '',
    '16-50',
    'a',
    'Foo',
    '12.1',
    '-12',
    -12,
    '_',
])
def test_fail_space(value):
    assert v.space().validate(value) is False

    with pytest.raises(SpaceException, match=r' must contain only space characters'):
        assert v.space().check(value)
        assert v.space().claim(value)
