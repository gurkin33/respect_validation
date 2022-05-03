from respect_validation.Exceptions import ValidationException


class BytearrayTypeException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be bytearray type',
        },
        'negative': {
            'standard': '{name} must not be bytearray type',
        }
    }
