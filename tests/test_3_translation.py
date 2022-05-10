import json

from respect_validation import Validator as v, Factory
from respect_validation.Exceptions import NestedValidationException

with open(str(__file__).replace('test_3_translation.py', 'subjects/one_language.json')) as json_file:
    one_language = json.load(json_file)

with open(str(__file__).replace('test_3_translation.py', 'subjects/several_languages.json')) as json_file:
    several_languages = json.load(json_file)


Factory.set_translation(one_language)


def test_one_language_1():

    try:
        v.numericVal().positive().between(1, 255).claim('ggg')
        assert False
    except NestedValidationException as nve:
        assert nve.get_messages() == {
            'numericVal': ['"ggg" muss numerisch sein'],
            'positive': ['"ggg" muss positiv sein']}


def test_one_language_2():

    try:
        v.numericVal().positive().between(1, 255).claim(-1)
        assert False
    except NestedValidationException as nve:
        assert nve.get_messages() == {
            'positive': ['"-1" muss positiv sein'],
            'between': ['"-1" muss zwischen 1 und 255 liegen']}


def test_one_language_3():
    Factory.set_translation({})
    try:
        v.numericVal().positive().between(1, 255).claim(-1)
        assert False
    except NestedValidationException as nve:
        assert nve.get_messages() == {
            'positive': ['"-1" must be positive'],
            'between': ['"-1" must be between 1 and 255']}


def test_one_language_4():
    one_language['numericVal']['default']['standard'] = 'Who is there? Is this message there?'
    Factory.set_translation(one_language)
    try:
        v.numericVal().positive().between(1, 255).claim('ggg')
        assert False
    except NestedValidationException as nve:
        assert nve.get_messages() == {
            'numericVal': ['Who is there? Is this message there?'],
            'positive': ['"ggg" muss positiv sein']}


def test_one_language_5():
    one_language['numericVal']['default']['standard'] = 'Who is {there}? Is this message {there}? {name}'
    Factory.set_translation(one_language)
    try:
        v.numericVal().positive().between(1, 255).claim('ggg')
        assert False
    except KeyError as k:
        assert str(k) == "'there'"

# Several languages tests


def test_languages_1():
    Factory.set_translation(several_languages).default_language('custom')
    try:
        v.numericVal().positive().between(1, 255).claim('ggg')
        assert False
    except NestedValidationException as nve:
        assert nve.get_messages() == {
            'numericVal': ['Is this "ggg" numeric? I don\'t think so...'],
            'positive': ['Is this "ggg" positive? I don\'t think so...']}


def test_languages_2():
    try:
        v.numericVal().positive().between(1, 255).set_language('de').claim('ggg')
        assert False
    except NestedValidationException as nve:
        assert nve.get_messages() == {
            'numericVal': ['"ggg" muss numerisch sein'],
            'positive': ['"ggg" muss positiv sein']}


def test_languages_3():
    try:
        v.numericVal().positive().between(1, 255).set_language('en').claim('ggg')
        assert False
    except NestedValidationException as nve:
        assert nve.get_messages() == {'numericVal': ['"ggg" must be numeric'], 'positive': ['"ggg" must be positive']}


def test_languages_4():
    try:
        v.numericVal().positive().between(1, 255).set_language('en123').claim('ggg')
        assert False
    except NestedValidationException as nve:
        assert nve.get_messages() == {
            'numericVal': ['Is this "ggg" numeric? I don\'t think so...'],
            'positive': ['Is this "ggg" positive? I don\'t think so...']}


def test_languages_5():
    Factory.set_translation(several_languages).default_language(None)
    try:
        v.numericVal().positive().between(1, 255).set_language('en123').claim('ggg')
        assert False
    except NestedValidationException as nve:
        assert nve.get_messages() == {'numericVal': ['"ggg" must be numeric'], 'positive': ['"ggg" must be positive']}


def test_languages_6():
    Factory.set_translation(several_languages).default_language(None)
    try:
        v.numericVal().positive().between(1, 255).set_language('custom').claim('ggg')
        assert False
    except NestedValidationException as nve:
        assert nve.get_messages() == {
            'numericVal': ['Is this "ggg" numeric? I don\'t think so...'],
            'positive': ['Is this "ggg" positive? I don\'t think so...']}
