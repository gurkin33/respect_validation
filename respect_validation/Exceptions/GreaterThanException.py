from respect_validation.Exceptions import ValidationException


class GreaterThanException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be greater than {_compare_to}',
        },
        'negative': {
            'standard': '{name} must not be greater than {_compare_to}',
        }
    }
