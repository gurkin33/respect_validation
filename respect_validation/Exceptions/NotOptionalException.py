from respect_validation.Exceptions import ValidationException


class NotOptionalException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must not be optional',
        },
        'negative': {
            'standard': '{name} must be optional',
        }
    }
