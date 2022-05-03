import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.ImageException import ImageException


@pytest.mark.parametrize('value', [
    str(__file__).replace('test_image.py', 'subjects/test_img.jpeg'),
    str(__file__).replace('test_image.py', 'subjects/test_img.gif'),
])
def test_success_image(value):
    assert v.image().validate(value)
    assert v.image().check(value) is None
    assert v.image().claim(value) is None


@pytest.mark.parametrize('value', [
    [],
    123456789,
    True,
    object(),
    '',
    'ABCDEFGHIKLMNOPQRSTVXYZ',
])
def test_fail_image(value):
    assert v.image().validate(value) is False

    with pytest.raises(ImageException, match=r' must be a valid image'):
        assert v.image().check(value)
        assert v.image().claim(value)
