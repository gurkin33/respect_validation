from respect_validation.Exceptions import ValidationException


class PrimeNumberException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a valid prime number',
        },
        'negative': {
            'standard': '{name} must not be a valid prime number',
        }
    }
