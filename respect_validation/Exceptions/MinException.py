from respect_validation.Exceptions.ValidationException import ValidationException


class MinException(ValidationException):
    INCLUSIVE = 'inclusive'

    _default_templates = {
        'default': {
            'standard': '{name} must be greater than or equal to {_compare_to}',
        },
        'negative': {
            'standard': '{name} must not be greater than or equal to {_compare_to}',
        }
    }
