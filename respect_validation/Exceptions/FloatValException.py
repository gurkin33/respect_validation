from respect_validation.Exceptions import ValidationException


class FloatValException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a float number',
        },
        'negative': {
            'standard': '{name} must not be a float number',
        }
    }
