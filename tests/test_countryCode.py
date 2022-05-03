import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions import ComponentException
from respect_validation.Exceptions.CountryCodeException import CountryCodeException
from respect_validation.Rules.CountryCode import CountryCode


@pytest.mark.parametrize('code_type,value', [
    [CountryCode.ALPHA2, 'BR'],
    [CountryCode.ALPHA3, 'BRA'],
    [CountryCode.NUMERIC, '076'],
    [CountryCode.ALPHA2, 'DE'],
    [CountryCode.ALPHA3, 'DEU'],
    [CountryCode.NUMERIC, '276'],
    [CountryCode.ALPHA2, 'US'],
    [CountryCode.ALPHA3, 'USA'],
    [CountryCode.NUMERIC, '840'],
])
def test_success_countryCode(code_type, value):
    assert v.countryCode(code_type).validate(value)
    assert v.countryCode(code_type).check(value) is None
    assert v.countryCode(code_type).claim(value) is None


@pytest.mark.parametrize('code_type,value', [
    [CountryCode.ALPHA2, 'USA'],
    [CountryCode.ALPHA3, 'US'],
    [CountryCode.NUMERIC, '000'],
])
def test_fail_countryCode(code_type, value):
    assert v.countryCode(code_type).validate(value) is False

    with pytest.raises(CountryCodeException, match="must be a valid country"):
        assert v.countryCode(code_type).check(value)
        assert v.countryCode(code_type).claim(value)


def test_fail_countryCode2():
    with pytest.raises(ComponentException, match="is not a valid set for ISO 3166"):
        assert v.countryCode('123123').validate('123123') is False
        assert v.countryCode('123123').check('123123')
        assert v.countryCode('123123').claim('123123')
