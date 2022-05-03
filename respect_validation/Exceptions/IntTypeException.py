from respect_validation.Exceptions import ValidationException


class IntTypeException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be of type integer',
        },
        'negative': {
            'standard': '{name} must not be of type integer',
        }
    }
