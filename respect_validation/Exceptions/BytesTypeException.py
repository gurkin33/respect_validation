from respect_validation.Exceptions import ValidationException


class BytesTypeException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be bytes type',
        },
        'negative': {
            'standard': '{name} must not be bytes type',
        }
    }
