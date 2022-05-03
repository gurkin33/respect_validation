from respect_validation.Exceptions import ValidationException


class PisException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a valid PIS number',
        },
        'negative': {
            'standard': '{name} must not be a valid PIS number',
        }
    }
