import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions import ValidationException, ComponentException
from respect_validation.Factory import Factory
from tests.Custom.Exceptions.CustomRuleException import CustomRuleException

Factory.add_rules_packages('tests.Custom.Rules')
Factory.add_exceptions_packages('tests.Custom.Exceptions')


def test_success_customRule():
    assert v.customRule().validate('Hello custom rule!')
    assert v.customRule().check('Hello custom rule!') is None
    assert v.customRule().claim('Hello custom rule!') is None


def test_fail_customRule():
    assert v.customRule().validate('Blah blah blah!') is False
    with pytest.raises(CustomRuleException, match=r'must be equal to.*Hello custom rule'):
        assert v.customRule().check('Blah blah blah!')
        assert v.customRule().claim('Blah blah blah!')


def test_fail_noExceptionRule():
    assert v.noExceptionRule().validate('Blah blah blah!') is False
    with pytest.raises(ValidationException, match=r'"Blah blah blah!" must be valid'):
        assert v.noExceptionRule().check('Blah blah blah!')
        assert v.noExceptionRule().claim('Blah blah blah!')


def test_fail_incorrectNameRule():
    with pytest.raises(ComponentException, match=r'Incorrect name of class in rule module IncorrectNameRule.py'):
        assert v.incorrectNameRule().validate('Blah blah blah!')
        assert v.incorrectNameRule().check('Blah blah blah!')
        assert v.incorrectNameRule().claim('Blah blah blah!')


def test_fail_moduleNotFound():
    with pytest.raises(ComponentException, match=r'ModuleNotFound is not a valid rule name'):
        assert v.moduleNotFound().validate('Blah blah blah!')
        assert v.moduleNotFound().check('Blah blah blah!')
        assert v.moduleNotFound().claim('Blah blah blah!')
