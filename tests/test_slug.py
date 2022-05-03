import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.SlugException import SlugException


@pytest.mark.parametrize('value', [
    'o-rato-roeu-o-rei-de-roma',
    'o-alganet-e-um-feio',
    'a-e-i-o-u',
    'anticonstitucionalissimamente',
])
def test_success_slug(value):
    assert v.slug().validate(value)
    assert v.slug().check(value) is None
    assert v.slug().claim(value) is None


@pytest.mark.parametrize('value', [
    '',
    'o-alganet-é-um-feio',
    'á-é-í-ó-ú',
    '-assim-nao-pode',
    'assim-tambem-nao-',
    'nem--assim',
    '--nem-assim',
    'Nem mesmo Assim',
    'Ou-ate-assim',
    '-Se juntar-tudo-Então-',
    'eAssim-vai',
    '@-!teste-teste',
    '*teste-teste',
    123,
    [],
    123.321,
    object(),
])
def test_fail_slug(value):
    assert v.slug().validate(value) is False

    with pytest.raises(SlugException, match=r' must be a valid slug'):
        assert v.slug().check(value)
        assert v.slug().claim(value)
