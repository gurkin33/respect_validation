from respect_validation.Exceptions import ValidationException


class RomanException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a valid Roman numeral',
        },
        'negative': {
            'standard': '{name} must not be a valid Roman numeral',
        }
    }
