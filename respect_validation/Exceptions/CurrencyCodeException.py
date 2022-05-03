from respect_validation.Exceptions import ValidationException


class CurrencyCodeException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a valid currency'
        },
        'negative': {
            'standard': '{name} must not be a valid currency'
        }
    }
