from respect_validation.Exceptions import ValidationException


class TrueValException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} is not considered as "True"',
        },
        'negative': {
            'standard': '{name} is considered as "True"',
        }
    }
