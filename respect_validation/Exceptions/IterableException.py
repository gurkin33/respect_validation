from respect_validation.Exceptions import ValidationException


class IterableException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be iterable',
        },
        'negative': {
            'standard': '{name} must not be iterable',
        }
    }
