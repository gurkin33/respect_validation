from respect_validation.Exceptions import ValidationException


class EndsWithException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must end with {end_value}',
        },
        'negative': {
            'standard': '{name} must not end with {end_value}',
        }
    }
