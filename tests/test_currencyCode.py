import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions import ComponentException
from respect_validation.Exceptions.CurrencyCodeException import CurrencyCodeException
from respect_validation.Rules.CurrencyCode import CurrencyCode


@pytest.mark.parametrize('currency_type, value', [
    [None, 'EUR'],
    [None, 'GBP'],
    [None, 'XAU'],
    [None, 'xxx'],
    [CurrencyCode.ALPHA3, 'XBA'],
    [CurrencyCode.ALPHA3, 'XXX'],
    [CurrencyCode.NUMERIC, '784'],
    [CurrencyCode.NUMERIC, '971'],
    [CurrencyCode.NUMERIC, '008'],
])
def test_success_currencyCode(currency_type, value):
    if currency_type:
        assert v.currencyCode(currency_type).validate(value)
        assert v.currencyCode(currency_type).check(value) is None
        assert v.currencyCode(currency_type).claim(value) is None
    else:
        assert v.currencyCode().validate(value)
        assert v.currencyCode().check(value) is None
        assert v.currencyCode().claim(value) is None


@pytest.mark.parametrize('currency_type,value', [
    [None, 'BTC'],
    [None, 'GGP'],
    [None, 'USA'],
])
def test_fail_currencyCode(currency_type, value):
    assert v.currencyCode().validate(value) is False

    with pytest.raises(CurrencyCodeException, match=" must be a valid currency"):
        assert v.currencyCode().check(value)
        assert v.currencyCode().claim(value)


def test_fail_currencyCode2():

    with pytest.raises(ComponentException, match='is not a valid set for ISO 4217'):
        assert v.currencyCode('123123').validate('test')
        assert v.currencyCode('123123').check('test')
        assert v.currencyCode('123123').claim('test')
