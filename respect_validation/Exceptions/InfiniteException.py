from respect_validation.Exceptions import ValidationException


class InfiniteException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be an infinite number',
        },
        'negative': {
            'standard': '{name} must not be an infinite number',
        }
    }
