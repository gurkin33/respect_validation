import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.VersionException import VersionException


@pytest.mark.parametrize('value', [
    '1.0.0',
    '1.0.0-alpha',
    '1.0.0-alpha.1',
    '1.0.0-0.3.7',
    '1.0.0-x.7.z.92',
    '1.3.7+build.2.b8f12d7',
    '1.3.7-rc.1',
])
def test_success_version(value):
    assert v.version().validate(value)
    assert v.version().check(value) is None
    assert v.version().claim(value) is None


@pytest.mark.parametrize('value', [
    '',
    '1.3.7--',
    '1.3.7++',
    '1.2.3.4',
    '1.2.3.4-beta',
    'beta',
    True,
    None,
    ['1.0.0'],
    object(),
])
def test_fail_version(value):
    assert v.version().validate(value) is False

    with pytest.raises(VersionException, match=r' must be a version'):
        assert v.version().check(value)
        assert v.version().claim(value)
