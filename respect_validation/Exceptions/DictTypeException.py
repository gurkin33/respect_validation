from respect_validation.Exceptions import ValidationException


class DictTypeException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be of type dict',
        },
        'negative': {
            'standard': '{name} must not be of type dict',
        }
    }
