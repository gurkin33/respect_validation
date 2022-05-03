from respect_validation.Exceptions import ValidationException


class FiniteException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a finite number',
        },
        'negative': {
            'standard': '{name} must not be a finite number',
        }
    }
