from respect_validation.Exceptions import ValidationException


class EquivalentException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be equivalent to {compare_to}',
        },
        'negative': {
            'standard': '{name} must not be equivalent to {compare_to}',
        }
    }
