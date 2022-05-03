from respect_validation.Exceptions import NestedValidationException


class AnyOfException(NestedValidationException):

    _default_templates = {
        'default': {
            'standard': 'At least one of these rules must pass for {name}',
        },
        'negative': {
            'standard': 'At least one of these rules must not pass for {name}',
        }
    }
