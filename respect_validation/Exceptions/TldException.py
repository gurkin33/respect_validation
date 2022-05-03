from respect_validation.Exceptions import ValidationException


class TldException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a valid top-level domain name'
        },
        'negative': {
            'standard': '{name} must not be a valid top-level domain name'
        }
    }
