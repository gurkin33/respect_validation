from respect_validation.Exceptions import ValidationException


class NumberException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be number',
        },
        'negative': {
            'standard': '{name} must not be number',
        }
    }
