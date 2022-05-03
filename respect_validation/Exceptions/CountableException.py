from respect_validation.Exceptions import ValidationException


class CountableException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be countable'
        },
        'negative': {
            'standard': '{name} must not be countable'
        }
    }
