from respect_validation.Exceptions import ValidationException


class EmailException(ValidationException):

    _default_templates = {
        'default': {
            'standard': '{name} must be valid email',
        },
        'negative': {
            'standard': '{name} must not be an email',
        }
    }
