from respect_validation.Exceptions import ValidationException


class ReadableException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be readable',
        },
        'negative': {
            'standard': '{name} must not be readable',
        }
    }
