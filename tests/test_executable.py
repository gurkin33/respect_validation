import os

import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.ExecutableException import ExecutableException

test_file = str(__file__).replace('test_executable.py', 'subjects/executable_file.test')
os.chmod(test_file, 0o777)


@pytest.mark.parametrize('value', [
    test_file
])
def test_success_executable(value):
    if os.name == 'nt':
        assert True
        return
    assert v.executable().validate(value)
    assert v.executable().check(value) is None
    assert v.executable().claim(value) is None


@pytest.mark.parametrize('value', [
    __file__
])
def test_fail_executable(value):
    assert v.executable().validate(value) is False

    with pytest.raises(ExecutableException, match=r'test_executable.py" must be an executable file'):
        assert v.executable().check(value)
        assert v.executable().claim(value)
