import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions import ValidationException

test_data = {
    "bday": '1989-01-01',
    "graduation": '2001-01-02',
    "some_date": '2022-04-04'
}

test_data2 = {
    "d": '1989-01-99',
    "gr": '20-01-02',
    "some_date with long key": '2022-13-04'
}


def test_success_each():
    assert v.each(v.dateTime('%Y-%m-%d')).validate(test_data.values())
    assert v.each(v.dateTime('%Y-%m-%d')).check(test_data.values()) is None
    assert v.each(v.dateTime('%Y-%m-%d')).claim(test_data.values()) is None

    assert v.each(v.stringType().length(3, 11)).validate(test_data.keys())
    assert v.each(v.stringType().length(3, 11)).check(test_data.keys()) is None
    assert v.each(v.stringType().length(3, 11)).claim(test_data.keys()) is None

    assert v.call('keys', v.each(v.stringType().length(3, 11))).validate(test_data)
    assert v.call('keys', v.each(v.stringType().length(3, 11))).check(test_data) is None
    assert v.call('keys', v.each(v.stringType().length(3, 11))).claim(test_data) is None


def test_fail_each():

    assert v.each(v.dateTime('%Y-%m-%d')).validate(test_data2.values()) is False
    assert v.each(v.stringType().length(3, 11)).validate(test_data2.keys()) is False
    assert v.call('keys', v.each(v.stringType().length(3, 11))).validate(test_data2) is False

    with pytest.raises(ValidationException):
        assert v.each(v.dateTime('%Y-%m-%d')).check(test_data2.values())
        assert v.each(v.dateTime('%Y-%m-%d')).claim(test_data2.values())

        assert v.each(v.stringType().length(3, 11)).check(test_data2.keys())
        assert v.each(v.stringType().length(3, 11)).claim(test_data2.keys())

        assert v.call('keys', v.each(v.stringType().length(3, 11))).check(test_data2)
        assert v.call('keys', v.each(v.stringType().length(3, 11))).claim(test_data2)
