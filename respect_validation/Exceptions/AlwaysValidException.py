from respect_validation.Exceptions.ValidationException import ValidationException


class AlwaysValidException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} is always valid',
        },
        'negative': {
            'standard': '{name} is always invalid',
        }

    }
