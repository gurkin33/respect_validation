import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.BytearrayTypeException import BytearrayTypeException


@pytest.mark.parametrize('value', [
    bytearray(b'hello world!'),
    bytearray([94, 91, 101, 125])
])
def test_success_bytearrayType(value):
    assert v.bytearrayType().validate(value)
    assert v.bytearrayType().check(value) is None
    assert v.bytearrayType().claim(value) is None


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
def test_fail_bytearrayType(value):
    assert v.bytearrayType().validate(value) is False

    with pytest.raises(BytearrayTypeException, match="must be bytearray type"):
        assert v.bytearrayType().check(value)
        assert v.bytearrayType().claim(value)
