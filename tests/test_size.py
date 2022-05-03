import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions import ComponentException
from respect_validation.Exceptions.SizeException import SizeException

test_file1 = str(__file__).replace('test_size.py', 'subjects/test_img_not_readable.jpeg')
test_file2 = str(__file__).replace('test_size.py', 'subjects/test_img.jpeg')
test_file3 = str(__file__).replace('test_size.py', 'subjects/test_img.gif')


@pytest.mark.parametrize('size, value', [
    [('1kb', None), test_file1],
    [('1KB', None), test_file1],
    [(None, '150kb'), test_file2],
    [('60kb', '100kb'), test_file3],
    [('60kb', '20mb'), test_file2],
    [('60KB', '20MB'), test_file2],
])
def test_success_size(size, value):
    assert v.size(*size).validate(value)
    assert v.size(*size).check(value) is None
    assert v.size(*size).claim(value) is None


@pytest.mark.parametrize('size, value', [
    [('10mb', None), test_file1],
    [(None, '50kb'), test_file2],
    [('100mb', '10gb'), test_file3],
    [('20mb', None), test_file2],
])
def test_fail_size(size, value):
    assert v.size(*size).validate(value) is False

    with pytest.raises(SizeException, match=r'(must.*be between|must.*be greater than|must.*be lower than)'):
        assert v.size(*size).check(value)
        assert v.size(*size).claim(value)


@pytest.mark.parametrize('size, value', [
    [(None, '100AAA'), test_file2],
    [('mb', None), test_file3],
])
def test_fail_size2(size, value):

    with pytest.raises(ComponentException, match=r'(is not a recognized file size)'):
        assert v.size(*size).check(value)
        assert v.size(*size).claim(value)
        assert v.size(*size).validate(value)


@pytest.mark.parametrize('size, value', [
    [(None, None), test_file1],
    [(True, True), test_file2],
])
def test_fail_size3(size, value):

    with pytest.raises(ComponentException, match=r'Set correct file size, for example'):
        assert v.size(*size).check(value)
        assert v.size(*size).claim(value)
        assert v.size(*size).validate(value)
