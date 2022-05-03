from respect_validation.Exceptions import ValidationException


class StringValException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a string',
        },
        'negative': {
            'standard': '{name} must not be string',
        }
    }
