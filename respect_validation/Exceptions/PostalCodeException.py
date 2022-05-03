from respect_validation.Exceptions import ValidationException


class PostalCodeException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a valid postal code on {country_code}',
        },
        'negative': {
            'standard': '{name} must not be a valid postal code on {country_code}',
        }
    }
