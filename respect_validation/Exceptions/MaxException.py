from respect_validation.Exceptions.ValidationException import ValidationException


class MaxException(ValidationException):
    INCLUSIVE = 'inclusive'

    _default_templates = {
        'default': {
            'standard': '{name} must be less than or equal to {_compare_to}',
        },
        'negative': {
            'standard': '{name} must not be less than or equal to {_compare_to}',
        }
    }
