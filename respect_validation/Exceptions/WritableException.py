from respect_validation.Exceptions import ValidationException


class WritableException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be writable',
        },
        'negative': {
            'standard': '{name} must not be writable',
        },
    }
