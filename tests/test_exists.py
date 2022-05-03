import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.ExistsException import ExistsException


@pytest.mark.parametrize('value', [
    __file__
])
def test_success_exists(value):
    assert v.exists().validate(value)
    assert v.exists().check(value) is None
    assert v.exists().claim(value) is None


@pytest.mark.parametrize('value', [
    '/some/path',
    None,
    True,
    [],
    object(),
    1
])
def test_fail_exists(value):
    assert v.exists().validate(value) is False

    with pytest.raises(ExistsException, match=r' must exists'):
        assert v.exists().check(value)
        assert v.exists().claim(value)
