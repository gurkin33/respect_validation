from respect_validation.Exceptions import ValidationException


class PositiveException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be positive',
        },
        'negative': {
            'standard': '{name} must not be positive',
        }
    }
