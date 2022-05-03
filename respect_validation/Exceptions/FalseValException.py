from respect_validation.Exceptions import ValidationException


class FalseValException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} is not considered as "False"',
        },
        'negative': {
            'standard': '{name} is considered as "False"',
        }
    }
