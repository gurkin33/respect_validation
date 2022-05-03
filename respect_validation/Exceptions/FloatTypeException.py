from respect_validation.Exceptions import ValidationException


class FloatTypeException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be of type float',
        },
        'negative': {
            'standard': '{name} must not be of type float',
        }
    }
