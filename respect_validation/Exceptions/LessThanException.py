from respect_validation.Exceptions import ValidationException


class LessThanException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be less than {_compare_to}',
        },
        'negative': {
            'standard': '{name} must not be less than {_compare_to}',
        }
    }
