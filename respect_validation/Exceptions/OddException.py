from respect_validation.Exceptions import ValidationException


class OddException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be an odd number',
        },
        'negative': {
            'standard': '{name} must not be an odd number',
        }
    }
