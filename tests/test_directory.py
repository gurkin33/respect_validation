import os

import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.DirectoryException import DirectoryException


@pytest.mark.parametrize('value', [
    __file__.replace('/test_directory.py', ''),
    __file__.replace('test_directory.py', ''),
    __file__.replace('test_directory.py', 'subjects')
])
def test_success_directory(value):
    if os.name == 'nt':
        assert True
        return
    assert v.directory().validate(value)
    assert v.directory().check(value) is None
    assert v.directory().claim(value) is None


@pytest.mark.parametrize('value', [
    __file__,
    object(),
    1,
    True,
    'abc'
])
def test_fail_directory(value):
    assert v.directory().validate(value) is False

    with pytest.raises(DirectoryException, match="must be a directory"):
        assert v.directory().check(value)
        assert v.directory().claim(value)
