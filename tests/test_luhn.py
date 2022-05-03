import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.LuhnException import LuhnException


@pytest.mark.parametrize('value', [
    '2222400041240011',
    '340316193809364',
    6011000990139424,
])
def test_success_luhn(value):
    assert v.luhn().validate(value)
    assert v.luhn().check(value) is None
    assert v.luhn().claim(value) is None


@pytest.mark.parametrize('value', [
    '2222400041240021',
    340316193809334,
    222240004124001.1,
    True,
    False,
    '',
    object(),
    [2222400041240011],
])
def test_fail_luhn(value):
    assert v.luhn().validate(value) is False

    with pytest.raises(LuhnException, match=r'must be a valid Luhn number'):
        assert v.luhn().check(value)
        assert v.luhn().claim(value)
