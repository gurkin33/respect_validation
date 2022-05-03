from respect_validation.Exceptions import NestedValidationException


class EachException(NestedValidationException):

    _default_templates = {
        'default': {
            'standard': 'Each item in {name} must be valid',
        },
        'negative': {
            'standard': 'Each item in {name} must not validate',
        }
    }
