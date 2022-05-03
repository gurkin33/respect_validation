from respect_validation.Exceptions import ValidationException


class ContainsAnyException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must contain at least one of the values {needles}'
        },
        'negative': {
            'standard': '{name} must not contain any of the values {needles}'
        }
    }
