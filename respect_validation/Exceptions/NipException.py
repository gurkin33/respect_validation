from respect_validation.Exceptions import ValidationException


class NipException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a valid Polish VAT identification number',
        },
        'negative': {
            'standard': '{name} must not be a valid Polish VAT identification number',
        }
    }
