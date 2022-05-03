import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.IntValException import IntValException


@pytest.mark.parametrize('value', [
    16,
    '165',
    123456,
    '06',
    '09',
    '0',
    '00',
    0b101010,
    0x2a,
    '089',
    True,
    False
])
def test_success_intVal(value):
    assert v.intVal().validate(value)
    assert v.intVal().check(value) is None
    assert v.intVal().claim(value) is None


@pytest.mark.parametrize('value', [
    [],
    None,
    object(),
    '',
    'ABCDEFGHIKLMNOPQRSTVXYZ',
    '',
    'a',
    '1.0',
    1.0,
    ' ',
    'Foo',
    '1.44',
    1e-5,
    '089ab',
])
def test_fail_intVal(value):
    assert v.intVal().validate(value) is False

    with pytest.raises(IntValException, match=r' must be an integer number'):
        assert v.intVal().check(value)
        assert v.intVal().claim(value)
