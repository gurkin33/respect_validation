from respect_validation.Exceptions import ValidationException


class NullableException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be nullable',
        },
        'negative': {
            'standard': '{name} must not be null',
        }
    }
