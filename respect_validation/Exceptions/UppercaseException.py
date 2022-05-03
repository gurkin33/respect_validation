from respect_validation.Exceptions import ValidationException


class UppercaseException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be uppercase',
        },
        'negative': {
            'standard': '{name} must not be uppercase',
        }
    }
