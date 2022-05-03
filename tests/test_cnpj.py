import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.CnpjException import CnpjException


@pytest.mark.parametrize('value', [
    '32.063.364/0001-07',
    '24.663.454/0001-00',
    '57.535.083/0001-30',
    '24.760.428/0001-09',
    '27.355.204/0001-00',
    '36.310.327/0001-07',
    '38175021000110',
    '37550610000179',
    '12774546000189',
    '77456211000168',
    '02023077000102',
])
def test_success_cnpj(value):
    assert v.cnpj().validate(value)
    assert v.cnpj().check(value) is None
    assert v.cnpj().claim(value) is None


@pytest.mark.parametrize('value', [
    '12.345.678/9012-34',
    '11.111.111/1111-11',
    '00000000000000',
    '11111111111111',
    '22222222222222',
    '33333333333333',
    '44444444444444',
    '55555555555555',
    '66666666666666',
    '77777777777777',
    '88888888888888',
    '99999999999999',
    '12345678900123',
    '99299929384987',
    '84434895894444',
    '44242340000000',
    '1',
    '22',
    '123',
    '992999999999929384',
    '99-010-0.',
])
def test_fail_cnpj(value):
    assert v.cnpj().validate(value) is False

    with pytest.raises(CnpjException, match=" must be a valid CNPJ number"):
        assert v.cnpj().check(value)
        assert v.cnpj().claim(value)
