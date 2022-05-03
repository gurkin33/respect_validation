import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.PisException import PisException


@pytest.mark.parametrize('value', [
    '120.4454.683-5',
    '120.8995.084-8',
    '120.5146.8577',
    '120.01842459',
    '1.2.0.7.9.8.1.6.7.8.2',
    '12044546835',
    '12089950848',
    '12051468577',
    '12001842459',
    '12079816782',
    12079816782,
])
def test_success_pis(value):
    assert v.pis().validate(value)
    assert v.pis().check(value) is None
    assert v.pis().claim(value) is None


@pytest.mark.parametrize('value', [
    '',
    '000.0000.000-0',
    '000.0000.000-1',
    '111.2222.444-5',
    '999999999.99',
    '8.8.8.8.8.8.8.8.8.8.8',
    '693-3129-110-1',
    '698.1131-111.2',
    '11111111111',
    '22222222222',
    '12345678901',
    '99299929384',
    '84434895894',
    '44242340002',
    '1',
    '22',
    '123',
    '992999999999929384',
    False,
    [],
    object(),
])
def test_fail_pis(value):
    assert v.pis().validate(value) is False

    with pytest.raises(PisException, match=r' must be a valid PIS number'):
        assert v.pis().check(value)
        assert v.pis().claim(value)
