from respect_validation.Exceptions import ValidationException


class NumericValException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be numeric',
        },
        'negative': {
            'standard': '{name} must not be numeric',
        }
    }
