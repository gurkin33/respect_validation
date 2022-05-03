import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.CharsetException import CharsetException


@pytest.mark.parametrize('charset, value', [
    [('ASCII', ), '23'],
    [('windows-1251', ), 'ыыыыы'.encode('ISO-8859-5')],
    [('UTF-8', 'ASCII'), 'strawberry'],
    [('ASCII', ), 'strawberry'.encode().decode('ASCII')],
    [('UTF-8', ), '日本国'],
    [('UTF-8', ), 'açaí'],
    [('ISO-8859-1', ), 'açaí'.encode('ISO-8859-1')],
])
def test_success_charset(charset, value):
    assert v.charset(*charset).validate(value)
    assert v.charset(*charset).check(value) is None
    assert v.charset(*charset).claim(value) is None


@pytest.mark.parametrize('value', [
    ['日本国'],
    ['açaí'],
])
def test_fail_charset(value):
    assert v.charset('ASCII').validate(value) is False

    with pytest.raises(CharsetException, match=" must be in the \\['ASCII'\\] charset"):
        assert v.charset('ASCII').check(value)
        assert v.charset('ASCII').claim(value)
