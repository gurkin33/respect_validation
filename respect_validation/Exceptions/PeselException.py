from respect_validation.Exceptions import ValidationException


class PeselException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a valid PESEL',
        },
        'negative': {
            'standard': '{name} must not be a valid PESEL',
        }
    }
