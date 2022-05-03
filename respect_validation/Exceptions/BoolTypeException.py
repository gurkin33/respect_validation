from respect_validation.Exceptions import ValidationException


class BoolTypeException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be of type boolean',
        },
        'negative': {
            'standard': '{name} must not be of type boolean',
        }
    }
