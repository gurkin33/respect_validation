from respect_validation.Exceptions import ValidationException


class TimeException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a valid time in the format {sample}'
        },
        'negative': {
            'standard': '{name} must not be a valid time in the format {sample}'
        }
    }
