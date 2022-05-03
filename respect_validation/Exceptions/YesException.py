from respect_validation.Exceptions import ValidationException


class YesException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} is not considered as "Yes"',
        },
        'negative': {
            'standard': '{name} is considered as "Yes"',
        },
    }
