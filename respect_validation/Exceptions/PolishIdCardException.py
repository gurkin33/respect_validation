from respect_validation.Exceptions import ValidationException


class PolishIdCardException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a valid Polish Identity Card number',
        },
        'negative': {
            'standard': '{name} must not be a valid Polish Identity Card number',
        }
    }
