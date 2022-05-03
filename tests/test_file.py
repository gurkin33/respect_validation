import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.FileException import FileException


@pytest.mark.parametrize('value', [
    __file__
])
def test_success_file(value):
    assert v.file().validate(value)
    assert v.file().check(value) is None
    assert v.file().claim(value) is None


@pytest.mark.parametrize('value', [
    str(__file__).replace('test_file.py', ''),
    'anything',
    [],
    object(),
    True
])
def test_fail_file(value):
    assert v.file().validate(value) is False

    with pytest.raises(FileException, match=r'must be a file'):
        assert v.file().check(value)
        assert v.file().claim(value)
