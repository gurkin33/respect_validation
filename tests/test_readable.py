import os

import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.ReadableException import ReadableException

test_file = str(__file__).replace('test_readable.py', 'subjects/readable_file.test')
test_file_not_readable = str(__file__).replace('test_readable.py', 'subjects/test_img_not_readable.jpeg')
os.chmod(test_file, 0o666)
os.chmod(test_file_not_readable, 0o000)


@pytest.mark.parametrize('value', [
    test_file,
    __file__
])
def test_success_readable(value):
    if os.name == 'nt':
        assert True
        return
    assert v.readable().validate(value)
    assert v.readable().check(value) is None
    assert v.readable().claim(value) is None


@pytest.mark.parametrize('value', [
    test_file_not_readable
])
def test_fail_readable(value):
    assert v.readable().validate(value) is False

    with pytest.raises(ReadableException, match=r'test_img_not_readable.jpeg" must be readable'):
        assert v.readable().check(value)
        assert v.readable().claim(value)
    os.chmod(test_file_not_readable, 0o666)
