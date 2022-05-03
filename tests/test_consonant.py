import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.ConsonantException import ConsonantException


@pytest.mark.parametrize('additional, value', [
    [None, 'b'],
    [None, 'c'],
    [None, 'd'],
    [None, 'w'],
    [None, 'y'],
    [None, 'bcdfghklmnp'],
    [None, 'bcdfghklm np'],
    [None, 'qrst'],
    [None, "\nz\t"],
    [None, "zbcxwyrspq"],
    [('!@#$%^&*(){}', ), '!@#$%^&*(){} bc dfg'],
    [('[]?+=/\\-_|"\',<>.', ), "[]?+=/\\-_|\"',<>. \t \n bc dfg"],
])
def test_success_consonant(additional, value):
    if additional:
        assert v.consonant(*additional).validate(value)
        assert v.consonant(*additional).check(value) is None
        assert v.consonant(*additional).claim(value) is None
    else:
        assert v.consonant().validate(value)
        assert v.consonant().check(value) is None
        assert v.consonant().claim(value) is None


@pytest.mark.parametrize('value', [
    '',
    'a',
    None,
    '16',
    'aeiou',
    'Foo',
    -50,
    'basic',
    [],
    10,
    object()
])
def test_fail_consonant(value):
    assert v.consonant().validate(value) is False

    with pytest.raises(ConsonantException, match=" must contain only consonants"):
        assert v.consonant().check(value)
        assert v.consonant().claim(value)
