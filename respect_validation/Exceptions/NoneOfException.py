from respect_validation.Exceptions import NestedValidationException


class NoneOfException(NestedValidationException):

    _default_templates = {
        'default': {
            'standard': 'None of these rules must pass for {name}',
        },
        'negative': {
            'standard': 'All of these rules must pass for {name}',
        }
    }
