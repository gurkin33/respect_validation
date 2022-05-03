from respect_validation.Exceptions import ValidationException


class PhoneException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a valid telephone number',
        },
        'negative': {
            'standard': '{name} must not be a valid telephone number',
        }
    }
