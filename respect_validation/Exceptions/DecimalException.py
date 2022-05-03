from respect_validation.Exceptions import ValidationException


class DecimalException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must have {decimals} decimals'
        },
        'negative': {
            'standard': '{name} must not have {decimals} decimals'
        }
    }
