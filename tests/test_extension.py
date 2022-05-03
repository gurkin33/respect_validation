import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.ExtensionException import ExtensionException


@pytest.mark.parametrize('extension,value', [
    ['py', __file__],
    ['txt', 'filename.txt'],
    ['jpg', 'filename.jpg'],
    ['inc', 'filename.inc'],
    ['bz2', 'filename.foo.bar.bz2'],
])
def test_success_extension(extension, value):
    assert v.extension(extension).validate(value)
    assert v.extension(extension).check(value) is None
    assert v.extension(extension).claim(value) is None


@pytest.mark.parametrize('extension,value', [
    ['txt', __file__],
    ['py2', __file__],
    ['jpg', 'filename.txt'],
    ['txt', 'filename.jpg'],
    ['bz2', 'filename.inc'],
    ['inc', 'filename.foo.bar.bz2'],
])
def test_fail_extension(extension, value):
    assert v.extension(extension).validate(value) is False

    with pytest.raises(ExtensionException, match=r' must have .* extension'):
        assert v.extension(extension).check(value)
        assert v.extension(extension).claim(value)
