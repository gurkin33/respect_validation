from respect_validation.Exceptions import ValidationException


class BaseNumException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a number in the base {base}',
        },
        'negative': {
            'standard': '{name} must not be a number in the base {base}',
        }
    }
