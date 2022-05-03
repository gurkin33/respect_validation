import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.PhoneException import PhoneException


@pytest.mark.parametrize('value', [
    '+5-555-555-5555',
    '+5 555 555 5555',
    '+5.555.555.5555',
    '+5(555)555.5555',
    '+5(555)555 5555',
    '+5(555)555-5555',
    '+5(555)5555555',
    '+33(1)22 22 22 22',
    '+1 (555) 555 5555',
    '+7 (555) 555 5555',
    '+7 (999) 555 5555',
])
def test_success_phone(value):
    assert v.phone().validate(value)
    assert v.phone().check(value) is None
    assert v.phone().claim(value) is None


@pytest.mark.parametrize('value', [
    '',
    '123',
    '(11- 97777-7777',
    '-11) 97777-7777',
    's555-5555',
    '555-555',
    '555555',
    '555+5555',
    '(555)555555',
    '(555)55555',
    '+(555)555 555',
    '555)555 555',
    '(555)55 555',
    '(555)5555 555',
    '5(555)55 55555',
    '(5)555555',
    '03610666-5',
    'text',
    "555\n5555",
    [],
])
def test_fail_phone(value):
    assert v.phone().validate(value) is False

    with pytest.raises(PhoneException, match=r' must be a valid telephone number'):
        assert v.phone().check(value)
        assert v.phone().claim(value)
