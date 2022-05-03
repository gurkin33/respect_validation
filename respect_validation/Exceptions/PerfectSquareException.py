from respect_validation.Exceptions import ValidationException


class PerfectSquareException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a valid perfect square',
        },
        'negative': {
            'standard': '{name} must not be a valid perfect square',
        }
    }
