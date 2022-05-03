from respect_validation.Exceptions import ValidationException


class NotEmptyException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must not be empty',
        },
        'negative': {
            'standard': '{name} must be empty',
        }
    }
