import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.MimetypeException import MimetypeException


@pytest.mark.parametrize('left, value', [
    ['image/gif', str(__file__).replace('test_mimetype.py', 'subjects/test_img.gif')],
    ['image/jpeg', str(__file__).replace('test_mimetype.py', 'subjects/test_img.jpeg')],
])
def test_success_mimetype(left, value):
    assert v.mimetype(left).validate(value)
    assert v.mimetype(left).check(value) is None
    assert v.mimetype(left).claim(value) is None


@pytest.mark.parametrize('left, value', [
    ['image/jpeg', str(__file__).replace('test_mimetype.py', 'subjects/test_img.gif')],
    ['image/gif', str(__file__).replace('test_mimetype.py', 'subjects/test_img.jpeg')],
    ['text/text', str(__file__)],
])
def test_fail_mimetype(left, value):
    assert v.mimetype(left).validate(value) is False

    with pytest.raises(MimetypeException, match=r'must have .* MIME type'):
        assert v.mimetype(left).check(value)
        assert v.mimetype(left).claim(value)
