import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.NipException import NipException


@pytest.mark.parametrize('value', [
    '1645865777',
    '5581418257',
    '1298727531',
])
def test_success_nip(value):
    assert v.nip().validate(value)
    assert v.nip().check(value) is None
    assert v.nip().claim(value) is None


@pytest.mark.parametrize('value', [
    [],
    object(),
    '1645865778',
    '164-586-57-77',
    '164-58-65-777',
    '5581418258',
    '1298727532',
    '1234567890',
])
def test_fail_nip(value):
    assert v.nip().validate(value) is False

    with pytest.raises(NipException, match=r' must be a valid Polish VAT identification number'):
        assert v.nip().check(value)
        assert v.nip().claim(value)
