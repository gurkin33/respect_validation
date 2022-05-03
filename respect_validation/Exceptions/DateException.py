from respect_validation.Exceptions import ValidationException


class DateException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be a valid date in the format {sample}'
        },
        'negative': {
            'standard': '{name} must not be a valid date in the format {sample}'
        }
    }
