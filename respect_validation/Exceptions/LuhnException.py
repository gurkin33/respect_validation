from respect_validation.Exceptions import ValidationException


class LuhnException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a valid Luhn number'
        },
        'negative': {
            'standard': '{name} must not be a valid Luhn number'
        }
    }
