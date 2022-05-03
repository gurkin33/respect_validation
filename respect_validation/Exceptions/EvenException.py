from respect_validation.Exceptions import ValidationException


class EvenException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be an even number',
        },
        'negative': {
            'standard': '{name} must not be an even number',
        }
    }
