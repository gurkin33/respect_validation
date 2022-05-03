from respect_validation.Exceptions import ValidationException


class IbanException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a valid IBAN',
        },
        'negative': {
            'standard': '{name} must not be a valid IBAN',
        }
    }
