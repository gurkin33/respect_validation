from respect_validation.Exceptions import ValidationException


class StringTypeException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be of type string'
        },
        'negative': {
            'standard': '{name} must not be of type string'
        }
    }
