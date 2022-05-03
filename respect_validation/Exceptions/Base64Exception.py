from respect_validation.Exceptions import ValidationException


class Base64Exception(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be Base64-encoded',
        },
        'negative': {
            'standard': '{name} must not be Base64-encoded',
        }
    }
