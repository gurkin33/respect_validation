from respect_validation.Exceptions import ValidationException


class CallableTypeException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be callable',
        },
        'negative': {
            'standard': '{name} must not be callable',
        }
    }
