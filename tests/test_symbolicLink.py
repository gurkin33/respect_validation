import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.SymbolicLinkException import SymbolicLinkException

test_file = str(__file__).replace('test_symbolicLink.py', 'subjects/test_img.gif.symbolic_link')


@pytest.mark.parametrize('value', [
    test_file
])
def test_success_symbolicLink(value):
    assert v.symbolicLink().validate(value)
    assert v.symbolicLink().check(value) is None
    assert v.symbolicLink().claim(value) is None


@pytest.mark.parametrize('value', [
    __file__
])
def test_fail_symbolicLink(value):
    assert v.symbolicLink().validate(value) is False

    with pytest.raises(SymbolicLinkException, match=r'test_symbolicLink.py" must be a symbolic link'):
        assert v.symbolicLink().check(value)
        assert v.symbolicLink().claim(value)
