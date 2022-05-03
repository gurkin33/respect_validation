import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.ListTypeException import ListTypeException


@pytest.mark.parametrize('value', [
    list(),
    [],
    [1, 'a']
])
def test_success_listType(value):
    assert v.listType().validate(value)
    assert v.listType().check(value) is None
    assert v.listType().claim(value) is None


@pytest.mark.parametrize('value', [
     dict(),
     object(),
     False,
     '',
     -2,
     0,
])
def test_fail_listType(value):
    assert v.listType().validate(value) is False

    with pytest.raises(ListTypeException, match=r' must be of type list'):
        assert v.listType().check(value)
        assert v.listType().claim(value)
