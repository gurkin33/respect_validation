import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.DictTypeException import DictTypeException


@pytest.mark.parametrize('value', [
    dict(),
    {},
    {'name': 'alexey'}
])
def test_success_dictType(value):
    assert v.dictType().validate(value)
    assert v.dictType().check(value) is None
    assert v.dictType().claim(value) is None


@pytest.mark.parametrize('value', [
     list(),
     object(),
     False,
     '',
     -2,
     0,
])
def test_fail_dictType(value):
    assert v.dictType().validate(value) is False

    with pytest.raises(DictTypeException, match=r' must be of type dict'):
        assert v.dictType().check(value)
        assert v.dictType().claim(value)
