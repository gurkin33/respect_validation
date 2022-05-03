import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.YesException import YesException


@pytest.mark.parametrize('value', [
    'Y',
    'Yea',
    'Yeah',
    'Yep',
    'Yes',
])
def test_success_yes(value):
    assert v.yes().validate(value)
    assert v.yes().check(value) is None
    assert v.yes().claim(value) is None


@pytest.mark.parametrize('value', [
    'Si',
    'Sim',
    'Yoo',
    True,
    ['Yes'],
    object(),
])
def test_fail_yes(value):
    assert v.yes().validate(value) is False

    with pytest.raises(YesException, match=r' is not considered as'):
        assert v.yes().check(value)
        assert v.yes().claim(value)
