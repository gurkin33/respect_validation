from respect_validation.Exceptions import ValidationException


class NoException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} is not considered as "No"',
        },
        'negative': {
            'standard': '{name} is considered as "No"',
        }
    }
