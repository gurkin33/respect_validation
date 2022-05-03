import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions import ComponentException
from respect_validation.Exceptions.PostalCodeException import PostalCodeException


@pytest.mark.parametrize('country_code,value', [
    ['BR', '02179-000'],
    ['BR', '02179000'],
    ['CA', 'A1A 2B2'],
    ['GB', 'GIR 0AA'],
    ['GB', 'PR1 9LY'],
    ['US', '02179'],
    ['PL', '99-300'],
    ['NL', '1012 GX'],
    ['NL', '1012GX'],
    ['PT', '3660-606'],
    ['PT', '3660606'],
    ['CO', '110231'],
    ['KR', '03187'],
    ['IE', 'H53 R2E0'],
    ['IE', 'D6W 3333'],
    ['EC', '170515'],
    ['IL', '7019900'],
    ['IL', '94142'],
    ['KY', 'KY1-1102'],
    ['KY', 'KY2-2001'],
    ['KY', 'KY2-2001'],
    ['KY', 'KY3-2500'],
    ['AM', '0010'],
    ['RS', '24430'],
    ['GR', '24430'],
    ['GR', '244 30'],
    ['RU', '123456'],
])
def test_success_postalCode(country_code, value):
    assert v.postalCode(country_code).validate(value)
    assert v.postalCode(country_code).check(value) is None
    assert v.postalCode(country_code).claim(value) is None


@pytest.mark.parametrize('country_code,value', [
    ['BR', '02179'],
    ['BR', '02179.000'],
    ['CA', '1A1B2B'],
    ['GB', 'GIR 00A'],
    ['GB', 'GIR0AA'],
    ['GB', 'PR19LY'],
    ['US', '021 79'],
    ['PL', '99300'],
    ['KR', '548940'],
    ['KR', '548-940'],
    ['EC', 'A1234B'],
    ['KY', 'KY4-2500'],
    ['AM', '375010'],
    ['RS', '244300'],
])
def test_fail_postalCode(country_code, value):
    assert v.postalCode(country_code).validate(value) is False

    with pytest.raises(PostalCodeException, match=r' must be a valid postal code on '):
        assert v.postalCode(country_code).check(value)
        assert v.postalCode(country_code).claim(value)


@pytest.mark.parametrize('country_code,value', [
    ['YE', ''],
    ['YE', '02179'],
    [None, '02179'],
    [None, None],
])
def test_fail_postalCode2(country_code, value):
    with pytest.raises(ComponentException, match=r'Cannot validate postal code from'):
        assert v.postalCode(country_code).validate(value)
        assert v.postalCode(country_code).check(value)
        assert v.postalCode(country_code).claim(value)
