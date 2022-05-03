from respect_validation.Exceptions import ValidationException


class CharsetException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be in the {charset} charset',
        },
        'negative': {
            'standard': '{name} must not be in the {charset} charset',
        }
    }
