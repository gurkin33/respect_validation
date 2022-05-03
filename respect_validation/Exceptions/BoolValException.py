from respect_validation.Exceptions import ValidationException


class BoolValException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a boolean value',
        },
        'negative': {
            'standard': '{name} must not be a boolean value',
        }
    }
