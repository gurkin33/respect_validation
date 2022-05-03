from respect_validation.Exceptions import ValidationException


class OptionalException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be optional',
        },
        'negative': {
            'standard': '{name} must not be optional',
        }
    }
