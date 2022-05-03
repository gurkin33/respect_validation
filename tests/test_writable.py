import os

import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.WritableException import WritableException

test_file = str(__file__).replace('test_writable.py', 'subjects/no_writable_file.test')
os.chmod(test_file, 0o555)


@pytest.mark.parametrize('value', [
    __file__
])
def test_success_writable(value):
    if os.name == 'nt':
        assert True
        return
    assert v.writable().validate(value)
    assert v.writable().check(value) is None
    assert v.writable().claim(value) is None


@pytest.mark.parametrize('value', [
    test_file
])
def test_fail_writable(value):
    assert v.writable().validate(value) is False

    with pytest.raises(WritableException, match=r'no_writable_file.test" must be writable'):
        assert v.writable().check(value)
        assert v.writable().claim(value)
    os.chmod(test_file, 0o666)
