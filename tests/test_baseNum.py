import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions import ComponentException
from respect_validation.Exceptions.BaseNumException import BaseNumException


@pytest.mark.parametrize('base, value', [
            [(2, ), '011010001'],
            [(3, ), '0120122001'],
            [(8, ), '01234567520'],
            [(16, ), '012a34f5675c20d'],
            [(20, ), '012ah34f5675hic20dj'],
            [(50, ), '012ah34f56A75FGhic20dj'],
            [(62, ), 'Z01xSsg5675hic20dj'],
            [(2, 'xy'), 'xyyxyxxy'],
            [(3, 'pfg'), 'gfpffp'],
])
def test_success_baseNum(base, value):
    assert v.baseNum(*base).validate(value)
    assert v.baseNum(*base).check(value) is None
    assert v.baseNum(*base).claim(value) is None


@pytest.mark.parametrize('base, value', [
    [(2, ), ''],
    [(3, ), ''],
    [(8, ), ''],
    [(16, ), ''],
    [(20, ), ''],
    [(50, ), ''],
    [(62, ), ''],
    [(2, ), '01210103001'],
    [(3, ), '0120125f2001'],
    [(8, ), '01234dfZ567520'],
    [(16, ), '012aXS34f5675c20d'],
    [(20, ), '012ahZX34f5675hic20dj'],
    [(50, ), '012ahGZ34f56A75FGhic20dj'],
    [(61, ), 'Z01xSsg5675hic20dj'],
])
def test_fail_baseNum(base, value):
    assert v.baseNum(*base).validate(value) is False

    with pytest.raises(BaseNumException, match="must be a number in the base"):
        assert v.baseNum(*base).check(value)
        assert v.baseNum(*base).claim(value)


@pytest.mark.parametrize('base, value', [
    [(None, ), ''],
    [('3', ), ''],
    [([], ), ''],
    [(1000, ), ''],
])
def test_fail_baseNum2(base, value):
    with pytest.raises(ComponentException, match=r'a base.*between 1 and 62'):
        assert v.baseNum(*base).validate(value)
        assert v.baseNum(*base).check(value)
        assert v.baseNum(*base).claim(value)
