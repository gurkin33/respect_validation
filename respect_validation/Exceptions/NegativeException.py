from respect_validation.Exceptions import ValidationException


class NegativeException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be negative',
        },
        'negative': {
            'standard': '{name} must not be negative',
        }
    }
