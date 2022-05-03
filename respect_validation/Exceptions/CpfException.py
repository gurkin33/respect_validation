from respect_validation.Exceptions import ValidationException


class CpfException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a valid CPF number'
        },
        'negative': {
            'standard': '{name} must not be a valid CPF number'
        }
    }
