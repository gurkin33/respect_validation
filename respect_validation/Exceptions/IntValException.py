from respect_validation.Exceptions import ValidationException


class IntValException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be an integer number',
        },
        'negative': {
            'standard': '{name} must not be an integer number',
        }
    }
