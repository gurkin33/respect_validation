from respect_validation.Exceptions import ValidationException


class IsbnException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a ISBN',
        },
        'negative': {
            'standard': '{name} must not be a ISBN',
        }
    }
