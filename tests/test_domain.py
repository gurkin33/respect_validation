import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.DomainException import DomainException


@pytest.mark.parametrize('tld_check, value', [
    [False, '111111111111domain.local'],
    [False, '111111111111.domain.local'],
    [True, 'example.com'],
    [True, 'xn--bcher-kva.ch'],
    [True, 'mail.xn--bcher-kva.ch'],
    [True, 'example-hyphen.com'],
    [True, 'example--valid.com'],
    [True, 'std--a.com'],
    [True, 'r--w.com'],
])
def test_success_domain(tld_check, value):
    if tld_check:
        assert v.domain().validate(value)
        assert v.domain().check(value) is None
        assert v.domain().claim(value) is None
    else:
        assert v.domain(tld_check).validate(value)
        assert v.domain(tld_check).check(value) is None
        assert v.domain(tld_check).claim(value) is None


@pytest.mark.parametrize('value', [
    None,
    object(),
    [],
    '',
    'no dots',
    '2222222domain.local',
    '-example-invalid.com',
    'example.invalid.-com',
    'xn--bcher--kva.ch',
    'example.invalid-.com',
    '1.2.3.256',
    '1.2.3.4',
])
def test_fail_domain(value):
    assert v.domain().validate(value) is False

    with pytest.raises(DomainException, match="must be a valid domain"):
        assert v.domain().check(value)
        assert v.domain().claim(value)
