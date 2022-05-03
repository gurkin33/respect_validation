import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions import ValidationException


@pytest.mark.parametrize('keySet, value', [
    [(v.key('foo', v.intVal().Between(1, 100).max(90)),
      v.key('bar', v.intVal().Between(1, 100).max(90))),
     {'foo': 42, 'bar': 73}],
    [(v.key('foo', v.intVal().Between(1, 100).max(90)),
      v.key('bar', v.intVal().Between(1, 100).max(90)),
      v.key('baz', v.intVal().Between(1, 100).max(90), False)),
     {'foo': 42, 'bar': 73}]
])
def test_success_keySet(keySet, value):
    assert v.keySet(*keySet).validate(value)
    assert v.keySet(*keySet).check(value) is None
    assert v.keySet(*keySet).claim(value) is None


@pytest.mark.parametrize('keySet, value', [
    [(v.key('foo', v.intVal().Between(1, 100).max(90)),
      v.key('bar', v.intVal().Between(1, 100).max(90))),
     {'foo': 42, 'bar': 120}],

    [(v.key('foo', v.intVal().Between(1, 100).max(90)),),
     {'foo': 42, 'bar': 120}],

    [(v.key('foo', v.intVal().Between(1, 100).max(90)),
      v.key('bar', v.intVal().Between(1, 100).max(90))),
     {'foo': 42}],

    [(v.key('foo', v.intVal().Between(1, 100).max(90)),
      v.key('bar', v.intVal().Between(1, 100).max(90))),
     {}],
    [(v.key('foo', v.intVal().Between(1, 100).max(90)),
      v.key('bar', v.intVal().Between(1, 100).max(90)),
      v.key('baz', v.intVal().Between(1, 100).max(90))),
     {'foo': 42, 'bar': 73}]
])
def test_fail_keySet(keySet, value):
    assert v.keySet(*keySet).validate(value) is False

    with pytest.raises(ValidationException, match=r'(Must have keys|bar must be between 1 and 100)'):
        assert v.keySet(*keySet).check(value)
        assert v.keySet(*keySet).claim(value)
