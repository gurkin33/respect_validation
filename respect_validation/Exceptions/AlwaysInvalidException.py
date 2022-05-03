from respect_validation.Exceptions.ValidationException import ValidationException


class AlwaysInvalidException(ValidationException):

    SIMPLE = 'simple'

    _default_templates = {
        'default': {
            'standard': '{name} is always invalid',
            'simple': '{name}  is not valid'
        },
        'negative': {
            'standard': '{name} is always valid',
            'simple': '{name}  is valid'
        },
    }
