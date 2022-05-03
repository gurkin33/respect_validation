import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.BytesTypeException import BytesTypeException


@pytest.mark.parametrize('value', [
    'alexey'.encode(),
    b'bytes',
    b'\xd0\x91\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b',
    b'2dLH)'
])
def test_success_bytesType(value):
    assert v.bytesType().validate(value)
    assert v.bytesType().check(value) is None
    assert v.bytesType().claim(value) is None


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
def test_fail_bytesType(value):
    assert v.bytesType().validate(value) is False

    with pytest.raises(BytesTypeException, match="must be bytes type"):
        assert v.bytesType().check(value)
        assert v.bytesType().claim(value)
