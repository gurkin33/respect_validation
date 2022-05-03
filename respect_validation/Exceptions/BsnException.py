from respect_validation.Exceptions import ValidationException


class BsnException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a BSN',
        },
        'negative': {
            'standard': '{name} must not be a BSN',
        }
    }
