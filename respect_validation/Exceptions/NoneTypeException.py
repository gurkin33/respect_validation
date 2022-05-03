from respect_validation.Exceptions import ValidationException


class NoneTypeException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be None type',
        },
        'negative': {
            'standard': '{name} must not be None type',
        }
    }
