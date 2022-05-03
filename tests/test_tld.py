import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.TldException import TldException


@pytest.mark.parametrize('value', [
    'br',
    'cafe',
    'com',
    'democrat',
    'eu',
    'gmbh',
    'us',
])
def test_success_tld(value):
    assert v.tld().validate(value)
    assert v.tld().check(value) is None
    assert v.tld().claim(value) is None


@pytest.mark.parametrize('value', [
    '1',
    1.0,
    'wrongtld',
    [],
    object(),
    True,
])
def test_fail_tld(value):
    assert v.tld().validate(value) is False

    with pytest.raises(TldException, match=r' must be a valid top-level domain name'):
        assert v.tld().check(value)
        assert v.tld().claim(value)
