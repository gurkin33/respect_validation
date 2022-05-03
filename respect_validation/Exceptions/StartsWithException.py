from respect_validation.Exceptions import ValidationException


class StartsWithException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must start with {start_value}',
        },
        'negative': {
            'standard': '{name} must not start with {start_value}',
        }
    }
