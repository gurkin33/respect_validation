from respect_validation.Exceptions import ValidationException


class ContainsException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must contain the value {contains_value}',
        },
        'negative': {
            'standard': '{name} must not contain the value {contains_value}',
        }
    }
