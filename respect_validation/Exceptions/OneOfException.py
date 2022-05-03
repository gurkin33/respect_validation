from respect_validation.Exceptions.NestedValidationException import NestedValidationException


class OneOfException(NestedValidationException):

    _default_templates = {
        'default': {
            'standard': 'Only one of these rules must pass for {name}',
        },
        'negative': {
            'standard': 'Only one of these rules must not pass for {name}',
        }
    }
