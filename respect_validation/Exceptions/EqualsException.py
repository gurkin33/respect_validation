from respect_validation.Exceptions import ValidationException


class EqualsException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be equal to {compare_to}',
        },
        'negative': {
            'standard': '{name} must not be equal to {compare_to}',
        }
    }
