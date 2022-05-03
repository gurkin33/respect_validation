import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.HexRgbColorException import HexRgbColorException


@pytest.mark.parametrize('value', [
    '#000',
    '#00000F',
    '#00000f',
    '#123',
    '#123456',
    '#FFFFFF',
    '#ffffff',
    '123123',
    'FFFFFF',
    'ffffff',
    '443',
])
def test_success_hexRgbColor(value):
    assert v.hexRgbColor().validate(value)
    assert v.hexRgbColor().check(value) is None
    assert v.hexRgbColor().claim(value) is None


@pytest.mark.parametrize('value', [
    '#0',
    '#0000G0',
    '#0FG',
    '#1234',
    '#AAAAAA1',
    '#S',
    '1234',
    'foo',
    5,
    443,
    1,
    [],
    object(),
    None,
])
def test_fail_hexRgbColor(value):
    assert v.hexRgbColor().validate(value) is False

    with pytest.raises(HexRgbColorException, match=r' must be a hex RGB color'):
        assert v.hexRgbColor().check(value)
        assert v.hexRgbColor().claim(value)
