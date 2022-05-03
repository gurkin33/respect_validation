import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.NoException import NoException


@pytest.mark.parametrize('value', [
    'N',
    'Nay',
    'Nix',
    'No',
    'Nope',
    'Not',
])
def test_success_no(value):
    assert v.no().validate(value)
    assert v.no().check(value) is None
    assert v.no().claim(value) is None


@pytest.mark.parametrize('value', [
    '',
    [],
    object(),
    0,
    -0,
    None,
    'a',
    ' ',
    'Yes',
])
def test_fail_no(value):
    assert v.no().validate(value) is False

    with pytest.raises(NoException, match=r'is not considered as '):
        assert v.no().check(value)
        assert v.no().claim(value)
