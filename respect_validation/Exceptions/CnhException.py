from respect_validation.Exceptions import ValidationException


class CnhException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a valid CNH number',
        },
        'negative': {
            'standard': '{name} must not be a valid CNH number',
        }
    }
