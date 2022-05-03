from respect_validation.Exceptions import ValidationException


class CountryCodeException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a valid country'
        },
        'negative': {
            'standard': '{name} must not be a valid country'
        }
    }
